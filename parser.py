import pdfplumber

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

def extract_sections(text):
    return {
        "text": text,
        "education": "Detected Education",
        "skills": "Detected Skills",
        "experience": "Detected Experience"
    }
