import os
import typst
import urllib.request
import ssl

def download_fonts():
    """Programmatically downloads state-of-the-art open-source fonts if missing."""
    os.makedirs("fonts", exist_ok=True)
    
    # Create an unverified SSL context to fix macOS certificate issues
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    fonts_to_download = {
        "Inter-Regular.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/static/Inter-Regular.ttf",
        "Inter-SemiBold.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/static/Inter-SemiBold.ttf",
        "Lora-Regular.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/lora/static/Lora-Regular.ttf",
        "Lora-SemiBold.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/lora/static/Lora-SemiBold.ttf",
        "Montserrat-Regular.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/static/Montserrat-Regular.ttf",
        "Montserrat-SemiBold.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/static/Montserrat-SemiBold.ttf"
    }
    
    for filename, url in fonts_to_download.items():
        filepath = os.path.join("fonts", filename)
        if not os.path.exists(filepath):
            try:
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                # Pass the custom SSL context here
                with urllib.request.urlopen(req, context=ctx) as response, open(filepath, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Warning: Could not download {filename}: {e}")

def sanitize(text):
    """Escapes Typst special characters to prevent compilation crashes."""
    if not isinstance(text, str):
        return ""
    return text.replace("<", r"\<").replace(">", r"\>").replace("@", r"\@")

def generate_pdf(cv_data, template_name="cv_template.typ", output_filename="Output/my_cv.pdf"):
    os.makedirs("Output", exist_ok=True)
    download_fonts() # Ensure fonts exist before compiling!
    
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r", encoding="utf-8") as file:
        typst_code = file.read()
        
    raw_contacts = [
        sanitize(cv_data.get("email", "")),
        sanitize(cv_data.get("phone", "")),
        sanitize(cv_data.get("linkedin", "")),
        sanitize(cv_data.get("github", ""))
    ]
    valid_contacts = [item.strip() for item in raw_contacts if item.strip()]
    contact_str = "  |  ".join(valid_contacts)
    
    skills_str = " • ".join([sanitize(s) for s in cv_data.get("skills", [])])

    projects = cv_data.get("projects", [])
    project_typst = ""
    valid_projects = [p for p in projects if p.get("Name", "").strip()]
    
    if valid_projects: 
        project_typst += '#text(size: 13pt, weight: "semibold", fill: rgb("#111827"))[Featured Technical Projects]\n'
        project_typst += '#v(-4pt)\n#line(length: 100%, stroke: 0.5pt + rgb("#e2e8f0"))\n#v(4pt)\n'
        
        for proj in valid_projects:
            name = sanitize(proj.get("Name", "").strip())
            link = sanitize(proj.get("Link", "").strip())
            desc = sanitize(proj.get("Description", "").strip())
            
            project_typst += f'#text(weight: "semibold")[{name}]'
            if link:
                clean_link = link.replace("https://", "").replace("http://", "")
                project_typst += f' - #link("https://{clean_link}")[{clean_link}]\n'
            else:
                project_typst += '\n'
                
            if desc:
                project_typst += f'#v(5pt)\n{desc}\n'
            project_typst += '#v(10pt)\n'
            
    typst_code = typst_code.replace("[[NAME]]", sanitize(cv_data.get("name", "")))
    typst_code = typst_code.replace("[[TITLE]]", sanitize(cv_data.get("title", "")))
    typst_code = typst_code.replace("[[CONTACT_INFO]]", contact_str)
    typst_code = typst_code.replace("[[SUMMARY]]", sanitize(cv_data.get("summary", "")))
    typst_code = typst_code.replace("[[EXPERIENCE]]", sanitize(cv_data.get("experience", "")))
    typst_code = typst_code.replace("[[EDUCATION]]", sanitize(cv_data.get("education", "")))
    typst_code = typst_code.replace("[[SKILLS]]", skills_str)
    typst_code = typst_code.replace("[[PROJECTS_SECTION]]", project_typst)
    
    temp_typ_path = "Output/temp_cv.typ"
    with open(temp_typ_path, "w", encoding="utf-8") as file:
        file.write(typst_code)
        
    try:
        # We now instruct the Typst compiler to use our newly downloaded local fonts!
        typst.compile(temp_typ_path, output=output_filename, font_paths=["fonts"])
        return True, output_filename
    except Exception as e:
        return False, str(e)
    finally:
        if os.path.exists(temp_typ_path):
            os.remove(temp_typ_path)