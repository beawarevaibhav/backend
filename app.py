from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import extract_text_from_pdf, extract_sections
from scorer import score_resume
from feedback import generate_feedback
import io

app = Flask(__name__)
CORS(app)  # Allow React frontend to access backend

@app.route('/api/grade', methods=['POST'])
def grade_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({"error": "Empty file"}), 400

    try:
        file_bytes = io.BytesIO(file.read())
        text = extract_text_from_pdf(file_bytes)
        sections = extract_sections(text)
        score = score_resume(sections)
        feedback = generate_feedback(sections)

        return jsonify({
            "score": score,
            "feedback": feedback
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
