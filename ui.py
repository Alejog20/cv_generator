import streamlit as st
import os
import base64
from generator import generate_pdf

# Set page to wide so we have room for the live preview!
st.set_page_config(page_title="Modern CV Generator", page_icon="📄", layout="wide")

def display_pdf(file_path):
    """Reads a PDF and embeds it securely into the Streamlit UI."""
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Embedding the PDF in an iframe
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

st.title("📄 Modern CV Generator")
st.markdown("Fill out your details and choose a template. Generate to see a live preview!")

# Create a two-column layout: Left for Inputs, Right for Preview
col_input, col_preview = st.columns([1.2, 1])

with col_input:
    with st.form("cv_inputs"):
        st.subheader("🎨 Template Selection")
        # Dropdown to pick the template file
        selected_template = st.selectbox(
            "Choose your CV design:",
            options=[
                "cv_template.typ", 
                "minimal_bold.typ", 
                "classic_serif.typ", 
                "executive_clean.typ",
                "two_col_tech.typ", 
                "editorial_accent.typ",
                "premium_grid.typ"
            ],
            format_func=lambda x: x.replace(".typ", "").replace("_", " ").title()
        )
        
        st.divider()

        st.subheader("1. Personal Details")
        name = st.text_input("Full Name", value="Jane Doe")
        title = st.text_input("Professional Title", value="Senior Developer")
        
        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input("Email", value="jane@example.com")
            linkedin = st.text_input("LinkedIn", value="linkedin.com/in/jane")
        with col2:
            phone = st.text_input("Phone", value="+1 555-0198")
            github = st.text_input("GitHub", value="github.com/jane")

        st.subheader("2. Professional Summary")
        summary = st.text_area("Summary", value="A highly skilled professional with experience in modern software architecture...", height=100)

        st.subheader("3. Experience")
        experience = st.text_area("Work History", value="Lead Developer @ Tech Inc (2020 - Present)\n- Led a team to scale cloud infrastructure.\n- Improved CI/CD pipelines.", height=150)

        st.subheader("4. Education")
        education = st.text_area("Academic Background", value="B.S. Computer Science - University of State (2018-2022)", height=100)

        st.subheader("5. Skills")
        skills_input = st.text_input("Core Skills", value="Python, AWS, Docker, Typst, React")

        st.subheader("6. Featured Projects (Optional)")
        default_projects = [{"Name": "AutoTester", "Link": "github.com/autotester", "Description": "A robust testing framework."}]
        edited_projects = st.data_editor(default_projects, num_rows="dynamic", width="stretch", hide_index=True)
        submitted = st.form_submit_button("Preview & Generate PDF", type="primary")

# Handling the submission and generating the PDF
if submitted:
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
        "projects": edited_projects
    }
    
    with st.spinner("Compiling your selected template..."):
        # We pass the selected_template variable to our generator!
        success, result = generate_pdf(cv_data, template_name=selected_template)
        
    if success:
        with col_preview:
            st.success("✅ Generation Successful! Live Preview Below:")
            display_pdf(result)
            
            with open(result, "rb") as pdf_file:
                st.download_button(
                    label="⬇ Download Final PDF",
                    data=pdf_file,
                    file_name=f"{name.replace(' ', '_')}_CV.pdf",
                    mime="application/pdf",
                    use_container_width="stretch"
                )
    else:
        st.error("Oops! We encountered an issue while generating your PDF.")
        st.code(f"Compiler Error: {result}", language="text")