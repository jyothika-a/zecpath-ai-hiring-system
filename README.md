Zecpath AI Hiring System

About the Project

This project is an AI-based hiring system that helps in screening resumes.
It can read resumes (PDF), extract skills, and match them with job requirements.

I built this project to understand how real hiring systems (ATS) work.

---

Features

- Read resume from PDF
- Extract skills using NLP
- Get email and phone number
- Give score based on skills
- Match resume with job description
- Rank multiple resumes

---

Project Structure

- parsers → resume parsing logic
- ats_engine → matching and ranking
- data → sample resumes
- tests → test files
- logs → log files

---

How to Run

1. Create virtual environment

python -m venv venv

2. Activate

venv\Scripts\activate

3. Install requirements

pip install -r requirements.txt

4. Install spaCy model

python -m spacy download en_core_web_sm

5. Run job matcher

python -m ats_engine.job_matcher

---

Testing

pytest

---

What I Learned

- How to work with Python projects
- How ATS systems work
- Basic NLP using spaCy
- How to structure a real project

---

Future Improvements

- Add UI (Streamlit)
- Improve scoring system
- Add more features

---

Author

Jyothika P S