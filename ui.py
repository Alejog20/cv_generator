import streamlit as st
import os
from generator import generate_pdf

st.set_page_config(page_title="Modern CV Generator", page_icon="📄", layout="centered")

st.title("📄 Modern CV Generator")
st.markdown("Fill out the forms below to dynamically generate a state-of-the-art PDF CV.")

with st.form("cv_inputs"):
    st.subheader("1. Personal Details")
    name = st.text_input("Full Name", placeholder="e.g. Alex Johnson")
    title = st.text_input("Professional Title", placeholder="e.g. Lead Machine Learning Engineer")
    
    col1, col2 = st.columns(2)
    with col1:
        email = st.text_input("Email", placeholder="alex@example.com")
        linkedin = st.text_input("LinkedIn Profile", placeholder="linkedin.com/in/alexjohnson")
    with col2:
        phone = st.text_input("Phone", placeholder="+1 555-0198")
        github = st.text_input("GitHub Profile (Optional)", placeholder="github.com/alexjohnson")

    st.subheader("2. Professional Summary")
    summary = st.text_area("Summary", placeholder="Briefly highlight your expertise and career goals...", height=100)

    st.subheader("3. Experience")
    st.caption("Tip: Write your role, company, and dates, followed by bullet points.")
    experience = st.text_area("Work History", placeholder="Senior Developer @ Tech Innovations (2022 - Present)\n- Led a team of 5 engineers...\n- Architected a cloud-native solution...", height=150)

    st.subheader("4. Education")
    education = st.text_area("Academic Background", placeholder="B.S. in Computer Science - University of State (2018-2022)", height=100)

    st.subheader("5. Skills")
    skills_input = st.text_input("Core Skills (comma separated)", placeholder="Python, Docker, React, AWS, Agile")

    st.subheader("6. Featured Technical Projects (Optional)")
    st.caption("Click the '+' to add a new project, or select a row and press Delete/Backspace to remove it.")
    
    # This creates an interactive table that users can add rows to dynamically
    default_projects = [{"Name": "", "Link": "", "Description": ""}]
    edited_projects = st.data_editor(
        default_projects,
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True
    )

    submitted = st.form_submit_button("Generate PDF CV", type="primary")

if submitted:
    # Package all inputs into our dictionary
    cv_data = {
        "name": name,
        "title": title,
        "email": email,
        "phone": phone,
        "linkedin": linkedin,
        "github": github,
        "summary": summary,
        "experience": experience,
        "education": education,
        "skills": [skill.strip() for skill in skills_input.split(",") if skill.strip()],
        "projects": edited_projects  # Passing our dynamic list of dictionaries directly!
    }
    
    with st.spinner("Compiling your state-of-the-art CV..."):
        output_path = generate_pdf(cv_data)
        
    st.success(f"Success! Your CV has been saved to the `{output_path}` folder.")
    
    with open(output_path, "rb") as pdf_file:
        st.download_button(
            label="⬇️ Download PDF Now",
            data=pdf_file,
            file_name=f"{name.replace(' ', '_')}_CV.pdf",
            mime="application/pdf"
        )