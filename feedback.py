import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_feedback(sections):
    try:
        text = sections["text"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that gives resume improvement suggestions."},
                {"role": "user", "content": f"Give specific feedback for improving this resume:\n\n{text}"}
            ]
        )
        feedback_text = response.choices[0].message.content.strip()
        return feedback_text.split("\n")  # split by lines for UI
    except Exception as e:
        return [f"Error generating feedback: {str(e)}"]
