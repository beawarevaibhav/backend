def generate_feedback(sections):
    feedback = []
    text = sections["text"].lower()
    
    if "education" not in text:
        feedback.append("Add an Education section.")
    if "skills" not in text:
        feedback.append("Mention relevant skills.")
    if "experience" not in text:
        feedback.append("Include your work experience.")
    
    return feedback
