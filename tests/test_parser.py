from parsers.resume_parser import extract_skills

def test_extract_skills():
    text = "I know python and sql"
    skills = extract_skills(text)
    
    assert "python" in skills
    assert "sql" in skills