import re
#type: ignore
import PyPDF2

SKILLS_DB = [
    "python", "java", "html", "css", "javascript", "react",
    "node.js", "sql", "excel", "power bi", "machine learning"
]

JOB_ROLE_SKILLS = {
    "data analyst": ["python", "sql", "excel", "power bi", "data analysis"],

    "frontend developer": ["html", "css", "javascript", "react"],

    "backend developer": [
        "Node.js", "MongoDB", "MySQL", 
        "PostgreSQL","MS SQL", "MongoDB", 
        "Redis", "Cassandra"
        ],

    "full stack developer": [
        "html", "css", "javascript", 
        "react", "python", 
        "Node.js" ,"Angular", "Vue.js", "Svelte", "Tailwind CSS", 
        "Bootstrap", "Material UI"
        ],

    "DevOps developer": [
        "Linux fundamentals & scripting",
        "Git & version control",
        "Jenkins", "GitHub Actions", "GitLab CI",
        "Ansible", "Puppet", "Chef",
        "Docker", "containerization","Kubernetes", "orchestration", "AWS", "Azure", "GCP",
        "Terraform", "CloudFormation",
        "Prometheus", "Grafana", "ELK", "CloudWatch",
        "Networking & security basics","Blue/Green", "Canary",
        "Testing & quality assurance",
        "Collaboration & Agile practices",
        "SRE", "observability", "cost optimization"

    ]
}

def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text.lower()

def extract_skills(text):
    return [skill for skill in SKILLS_DB if skill in text]

def analyze_resume(pdf_path, job_role):
    text = extract_text(pdf_path)
    skills = extract_skills(text)

    role_key = job_role.lower()
    required = JOB_ROLE_SKILLS.get(role_key, [])

    matched = list(set(skills) & set(required))
    missing = list(set(required) - set(skills))
    score = int((len(matched)/len(required)) * 100) if required else 0

    return {
     

        "matched": matched,
        "missing": missing,
        "all_skills": skills,
        "score": score
    }
   
