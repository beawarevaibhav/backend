
# feedback.py
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_feedback(sections):
    text = sections.get("text", "")

    prompt = f"""
    You are a professional resume reviewer.
    Analyze the following resume content and give personalized feedback, including:
    - Suggestions for improvement
    - Missing important sections
    - Role-specific enhancements

    Resume Content:
    {text}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional resume reviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        ai_feedback = response['choices'][0]['message']['content']
        return ai_feedback.split('\n')  # Returns list of feedback lines
    except Exception as e:
        return [f"Error generating feedback: {e}"]
