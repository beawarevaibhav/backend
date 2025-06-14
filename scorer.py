def score_resume(sections):
    score = 0
    text = sections["text"].lower()
    
    if "education" in text:
        score += 30
    if "skills" in text:
        score += 30
    if "experience" in text:
        score += 40
    
    return score
