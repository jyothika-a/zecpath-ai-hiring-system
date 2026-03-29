from parsers.resume_parser import extract_text_from_pdf, extract_skills, extract_contact_info, score_resume

import os

def rank_resumes(folder_path):
    results = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(folder_path, file)
            
            text = extract_text_from_pdf(file_path)
            skills = extract_skills(text)
            contact = extract_contact_info(text)
            score = score_resume(skills)
            
            results.append({
                "name": file,
                "skills": skills,
                "score": score,
                "contact": contact
            })
    
    # Sort by score (highest first)
    ranked = sorted(results, key=lambda x: x["score"], reverse=True)
    
    return ranked


if __name__ == "__main__":
    ranked_resumes = rank_resumes("data")
    
    for r in ranked_resumes:
        print(r)