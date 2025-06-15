def generate_feedback(sections):
    feedback = []
    text = sections.get("text", "").lower()

    # Custom rules based on content
    if "internship" in text and "experience" not in text:
        feedback.append("You mentioned internships — consider labeling them clearly under 'Experience'.")
    
    if "python" in text and "projects" not in text:
        feedback.append("You know Python — consider showcasing it with real-world projects.")

    if "b.tech" in text or "engineering" in text:
        feedback.append("Tailor your resume for engineering roles by adding technical achievements.")

    if "mba" in text:
        feedback.append("Highlight leadership roles or business-related achievements.")

    if "team player" in text:
        feedback.append("Instead of saying 'team player', give an example where you worked in a team.")

    if "linkedin.com" not in text:
        feedback.append("Include a link to your LinkedIn profile.")

    if len(text.split()) < 200:
        feedback.append("Your resume seems short — try adding more accomplishments.")

    if not feedback:
        feedback.append("Great job! Your resume looks solid.")

    return feedback
