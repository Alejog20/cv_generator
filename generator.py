import os
import typst

def sanitize(text):
    """Escapes Typst special characters to prevent compilation crashes."""
    if not isinstance(text, str):
        return ""
    # Escaping angle brackets so Typst reads them as raw text, not labels
    return text.replace("<", r"\<").replace(">", r"\>")

def generate_pdf(cv_data, template_name="cv_template.typ", output_filename="Output/my_cv.pdf"):
    os.makedirs("Output", exist_ok=True)
    
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r", encoding="utf-8") as file:
        typst_code = file.read()
        
    # Sanitize and format contact info
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
        project_typst += '#text(size: 14pt, weight: "bold", fill: rgb("#111827"))[Featured Technical Projects]\n'
        project_typst += '#line(length: 100%, stroke: 0.5pt + rgb("#e5e7eb"))\n'
        
        for proj in valid_projects:
            name = sanitize(proj.get("Name", "").strip())
            link = sanitize(proj.get("Link", "").strip())
            desc = sanitize(proj.get("Description", "").strip())
            
            project_typst += f'#text(weight: "bold")[{name}]'
            if link:
                clean_link = link.replace("https://", "").replace("http://", "")
                project_typst += f' - #link("https://{clean_link}")[{clean_link}]\n'
            else:
                project_typst += '\n'
                
            if desc:
                project_typst += f'#v(5pt)\n{desc}\n'
            
            project_typst += '#v(10pt)\n'
            
    # Inject sanitized data
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
        
    # Robust Error Handling
    try:
        typst.compile(temp_typ_path, output=output_filename)
        return True, output_filename
    except Exception as e:
        return False, str(e)
    finally:
        # We always want to clean up the temp file, even if compilation crashes
        if os.path.exists(temp_typ_path):
            os.remove(temp_typ_path)