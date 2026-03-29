import re

import spacy
nlp=spacy.load("en_core_web_sm")

import logging
logging.basicConfig(level=logging.INFO)

import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        
        for page in reader.pages:
            text += page.extract_text()
    
    return text


def extract_skills(text):
    skills_list = [
        "python", "java", "sql",
        "machine learning", "data science",
        "deep learning", "nlp"
    ]
    
    doc = nlp(text.lower())
    found_skills = set()
    
    for token in doc:
        if token.text in skills_list:
            found_skills.add(token.text)
    
    return list(found_skills)


def extract_contact_info(text):
    email = re.findall(r'\S+@\S+', text)
    phone = re.findall(r'\d{10}', text)
    
    return {
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None
    }


def score_resume(skills):
    weights = {
        "python": 20,
        "machine learning": 25,
        "data science": 20,
        "sql": 15,
        "excel": 10
    }
    
    score = 0
    
    for skill in skills:
        score += weights.get(skill, 5)
    
    return min(score, 100)


if __name__ == "__main__":
    logging.info("Starting resume parsing...")
    file_path = "data/sample_resume.pdf"

    
    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)
    score = score_resume(skills)
    contact=extract_contact_info(text)
    
    print("Skills:", skills)
    print("Score:", score)
    print("contact:",contact)