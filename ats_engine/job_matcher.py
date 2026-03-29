from parsers.resume_parser import extract_text_from_pdf, extract_skills
import os

def match_resume_to_job(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)
    
    # Assign weights to job skills
    weights = {
        "python": 25,
        "machine learning": 25,
        "data science": 20,
        "sql": 15,
        "excel": 10
    }
    
    score = 0
    matched_skills = []
    
    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
            score += weights.get(skill, 5)
    
    return min(score, 100), matched_skills


def rank_resumes_by_job(folder_path, job_description):
    results = []
    
    print("Scanning folder:", folder_path)  # Debug
    
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            print("Processing:", file)  # Debug
            
            file_path = os.path.join(folder_path, file)
            
            text = extract_text_from_pdf(file_path)
            score, matched_skills = match_resume_to_job(text, job_description)
            
            results.append({
                "name": file,
                "match_score": round(score, 2),
                "matched_skills": matched_skills
            })
    
    # Sort by score (highest first)
    ranked = sorted(results, key=lambda x: x["match_score"], reverse=True)
    
    return ranked


if __name__ == "__main__":
    print("Job Matcher Started 🚀")
    
    job_description = """
    Looking for a Python developer with knowledge in machine learning, SQL, and data science.
    """
    
    ranked_resumes = rank_resumes_by_job("data", job_description)
    
    print("\nFinal Ranking:\n")
    
    for r in ranked_resumes:
        print(r)