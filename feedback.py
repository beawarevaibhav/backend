def generate_feedback(sections):
    try:
        text = sections.get("text", "").lower()
        feedback = []

        # Check for LinkedIn link
        if "linkedin.com" not in text:
            feedback.append("Include a link to your LinkedIn profile.")

        # Check if resume has less than 200 words
        word_count = len(text.split())
        if word_count < 200:
            feedback.append("Your resume seems short — try adding more accomplishments.")

        # Check for experience
        if "experience" not in text:
            feedback.append("Include a work experience section with job titles and responsibilities.")

        # Check for skills
        if "skills" not in text:
            feedback.append("Add a 'Skills' section to highlight your technical and soft skills.")

        # If no issues found
        if not feedback:
            feedback.append("Great job! Your resume covers all essential aspects.")

        return feedback

    except Exception as e:
        return [f"Error generating feedback: {str(e)}"]
