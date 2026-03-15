import sys
import logging

logging.basicConfig(filename='cv_generator.log', level=logging.ERROR)

try:
    import weasyprint
    from jinja2 import Template
except ImportError as e:
    print(f"CRITICAL ERROR: Missing required Python libraries.\nDetails: {e}")
    sys.exit(1)

# 1. The CV Data (Blends your exact original structure with ScotiaGBS targeting)
cv_data = {
    "name": "ALEJANDRO GARCÍA",
    "title": "Automation Developer & Analyst", 
    "location": "Bogotá, Colombia",
    "github": "github.com/Alejog20",
    "linkedin": "linkedin.com/in/alejandro-garcia-38a9339a",
    "profile": [
        "Professional experienced in process automation, data analysis, and corporate operations support.",
        "3+ years of hands-on experience in Python scripting, dashboard creation (Power BI, Looker Studio), and process documentation.",
        "Skilled at turning technical information into clear and actionable reports to support cross functional teams and stakeholders."
    ],
    "skills": [
        "Python (Pandas, Requests, Numpy, Openpyxl, Async, Playwright, FastAPI, Flask, other)",
        "Object-Oriented Programming",
        "Git/GitHub | XML/CXML",
        "Linux CLI",
        "Process Automation & ETL",
        "SQL, NOSQL DBs",
        "Advanced Excel",
        "Salesforce & Jira",
        "Technical Documentation"
    ],
    "experience": [
        {
            "title": "Automation Analyst / Billing Expert",
            "company": "Iron Mountain Inc.",
            "dates": "Sep 2022 - Present",
            "location": "North America Support",
            "bullets": [
                "Provided billing support for North American clients and resolved complex billing discrepancies.",
                "Led 10+ Python automation initiatives for the Billing and Collections departments, actively reducing manual reporting time by 90%.",
                "Developed ETL workflows and Looker Studio dashboards for tracking billing KPIs.",
                "Documented internal processes and collaborated with cross-functional teams via Salesforce, Jira and internal tools."
            ]
        }
    ],
    "projects": [
        {
            "title": "Multi-Platform E-Commerce Scraper - v2.0",
            "tech": "Python • Playwright-Stealth • Async • ETL",
            "bullets": [
                "Engineered a multi platform scraper featuring robust data validation, offline testing, and advanced anti-detection features.",
                "Implemented Playwright-Stealth, smart retry logic, and highly scalable asynchronous architecture.",
                "Integrated the python engine with a Telegram Bot that serves as the main UI and control panel."
            ]
        },
        {
            "title": "CSV EDI File Processor",
            "tech": "Python • Pandas • Watchdog • Rich CLI",
            "bullets": [
                "Automated file processor that dynamically converts CSV and DAT files into XLSX ready to use files.",
                "Included a modern CLI interface with detailed logging and rigorous data integrity validation."
            ]
        },
        {
            "title": "Reddit API Data Extraction",
            "tech": "Python • REST API • Data Cleaning • CSV Export",
            "bullets": [
                "Developed a data extraction tool for processing Reddit posts/comments based on user input.",
                "Integrated OAuth2 authentication, applied data cleaning algorithms, and generated analysis ready CSV outputs."
            ]
        }
    ],
    "education": [
        {"degree": "Bachelor in International Business", "school": "Universidad Santo Tomás (in progress, 2026)"},
        {"degree": "Java Full Stack Development Bootcamp", "school": "Generation (2025)"},
        {"degree": "Backend Programming with Python", "school": "Universidad de Caldas (2022)"},
        {"degree": "AI with Python", "school": "LinkedIn Learning (2024)"},
        {"degree": "Advanced Scrum", "school": "Project Management Institute"}
    ]
}

# 2. The Advanced HTML/CSS Template (Replicates the original browser-print layout)
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        @page { 
            margin: 0.8in 0.8in; 
            size: A4;
        }
        body { 
            font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif; 
            color: #111; 
            line-height: 1.45; 
            font-size: 10.5pt; 
        }
        
        /* Header Section */
        .header-container { margin-bottom: 20px; }
        h1 { font-size: 28pt; font-weight: 800; margin: 0 0 5px 0; letter-spacing: 0.5px; color: #000; text-transform: uppercase; }
        .title { font-size: 14pt; color: #444; font-weight: 600; margin-bottom: 10px; }
        .contact-bar { font-size: 9.5pt; color: #333; margin-bottom: 20px; display: flex; gap: 15px; flex-wrap: wrap; }
        .contact-bar a { color: #0056b3; text-decoration: none; }
        
        /* Section Headers */
        h2 { 
            font-size: 13pt; 
            color: #000; 
            text-transform: uppercase; 
            font-weight: 700; 
            border-bottom: 2px solid #000; 
            padding-bottom: 3px; 
            margin-top: 22px; 
            margin-bottom: 12px; 
            letter-spacing: 0.5px;
        }
        
        /* General Layout */
        p { margin: 0 0 8px 0; }
        ul { margin: 0 0 15px 0; padding-left: 20px; }
        li { margin-bottom: 5px; }
        
        /* Two-Column Skills Grid */
        .skills-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4px 20px;
            margin-bottom: 15px;
        }
        .skill-item {
            font-size: 10pt;
            position: relative;
            padding-left: 12px;
        }
        .skill-item::before {
            content: "•";
            position: absolute;
            left: 0;
            color: #000;
        }
        
        /* Experience & Projects Header Flexbox */
        .item-header {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 4px;
        }
        .item-title { font-weight: 700; font-size: 11.5pt; color: #000; }
        .item-company { font-weight: 600; font-style: italic; color: #444; }
        .item-meta { font-size: 9.5pt; color: #555; text-align: right; }
        .project-tech { font-size: 9.5pt; color: #0056b3; font-weight: 600; margin-bottom: 6px; }

        /* Education list */
        .edu-item { margin-bottom: 6px; position: relative; padding-left: 15px;}
        .edu-item::before { content: "•"; position: absolute; left: 0; }
        .edu-degree { font-weight: 600; }
    </style>
</head>
<body>

    <div class="header-container">
        <h1>{{ data.name }}</h1>
        <div class="title">{{ data.title }}</div>
        <div class="contact-bar">
            <span>📍 {{ data.location }}</span>
            <span>|</span>
            <span>🔗 <a href="https://{{ data.github }}">GitHub</a></span>
            <span>|</span>
            <span>💼 <a href="https://{{ data.linkedin }}">LinkedIn</a></span>
        </div>
    </div>

    <h2>Professional Profile</h2>
    <div>
        {% for para in data.profile %}
            <p>{{ para }}</p>
        {% endfor %}
    </div>

    <h2>Technical Skills</h2>
    <div class="skills-grid">
        {% for skill in data.skills %}
            <div class="skill-item">{{ skill }}</div>
        {% endfor %}
    </div>

    <h2>Professional Experience</h2>
    {% for job in data.experience %}
        <div class="item-header">
            <div>
                <span class="item-title">{{ job.title }}</span> | 
                <span class="item-company">{{ job.company }}</span>
            </div>
            <div class="item-meta">
                {{ job.dates }} | {{ job.location }}
            </div>
        </div>
        <ul>
            {% for bullet in job.bullets %}
                <li>{{ bullet }}</li>
            {% endfor %}
        </ul>
    {% endfor %}

    <h2>Technical Projects & GitHub</h2>
    {% for project in data.projects %}
        <div class="item-header">
            <div class="item-title">{{ project.title }}</div>
        </div>
        <div class="project-tech">{{ project.tech }}</div>
        <ul>
            {% for bullet in project.bullets %}
                <li>{{ bullet }}</li>
            {% endfor %}
        </ul>
    {% endfor %}

    <h2>Education & Certifications</h2>
    {% for edu in data.education %}
        <div class="edu-item">
            <span class="edu-degree">{{ edu.degree }}</span> - {{ edu.school }}
        </div>
    {% endfor %}

</body>
</html>
"""

# 3. Encapsulated generation function
def generate_cv_pdf(output_filename="Alejandro_Garcia_Automation_CV.pdf") -> tuple[bool, str]:
    try:
        template = Template(html_template)
        rendered_html = template.render(data=cv_data)
        
        weasyprint.HTML(string=rendered_html).write_pdf(output_filename)
        return True, f"Successfully saved to {output_filename}"
    except Exception as e:
        error_msg = f"An unexpected error occurred: {str(e)}"
        logging.error(error_msg)
        return False, error_msg