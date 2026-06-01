import os
import typst

def generate_pdf(cv_data, template_name="cv_template.typ", output_filename="Output/my_cv.pdf"):
    # 1. Ensure the Output directory exists
    os.makedirs("Output", exist_ok=True)
    
    # 2. Read the Typst template file
    template_path = os.path.join("templates", template_name)
    with open(template_path, "r", encoding="utf-8") as file:
        typst_code = file.read()
        
    # 3. Smart Formatting for Contact Info
    raw_contacts = [
        cv_data.get("email", ""),
        cv_data.get("phone", ""),
        cv_data.get("linkedin", ""),
        cv_data.get("github", "")
    ]
    valid_contacts = [item.strip() for item in raw_contacts if item.strip()]
    contact_str = "  |  ".join(valid_contacts)
    
    # 4. Format the skills list
    skills_str = " • ".join(cv_data["skills"])

    # 5. Dynamically build the Technical Projects section (Handles multiple projects)
    projects = cv_data.get("projects", [])
    project_typst = ""
    
    # Filter out any empty rows the user might have accidentally left in the table
    valid_projects = [p for p in projects if p.get("Name", "").strip()]
    
    if valid_projects: 
        project_typst += '#text(size: 14pt, weight: "bold", fill: rgb("#111827"))[Featured Technical Projects]\n'
        project_typst += '#line(length: 100%, stroke: 0.5pt + rgb("#e5e7eb"))\n'
        
        for proj in valid_projects:
            name = proj.get("Name", "").strip()
            link = proj.get("Link", "").strip()
            desc = proj.get("Description", "").strip()
            
            # Add Name and optional Link
            project_typst += f'#text(weight: "bold")[{name}]'
            if link:
                clean_link = link.replace("https://", "").replace("http://", "")
                project_typst += f' - #link("https://{clean_link}")[{clean_link}]\n'
            else:
                project_typst += '\n'
                
            # Add Description
            if desc:
                project_typst += f'#v(5pt)\n{desc}\n'
            
            # Add some spacing between projects
            project_typst += '#v(10pt)\n'
            
    # 6. Inject all the data into our placeholders
    typst_code = typst_code.replace("[[NAME]]", cv_data["name"])
    typst_code = typst_code.replace("[[TITLE]]", cv_data["title"])
    typst_code = typst_code.replace("[[CONTACT_INFO]]", contact_str)
    typst_code = typst_code.replace("[[SUMMARY]]", cv_data["summary"])
    typst_code = typst_code.replace("[[EXPERIENCE]]", cv_data["experience"])
    typst_code = typst_code.replace("[[EDUCATION]]", cv_data["education"])
    typst_code = typst_code.replace("[[SKILLS]]", skills_str)
    typst_code = typst_code.replace("[[PROJECTS_SECTION]]", project_typst)
    
    # 7. Save the populated code to a temporary file
    temp_typ_path = "Output/temp_cv.typ"
    with open(temp_typ_path, "w", encoding="utf-8") as file:
        file.write(typst_code)
        
    # 8. Compile directly to PDF
    typst.compile(temp_typ_path, output=output_filename)
    
    # 9. Clean up temporary files
    if os.path.exists(temp_typ_path):
        os.remove(temp_typ_path)
        
    return output_filename