from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import extract_text_from_pdf, extract_sections
from scorer import score_resume
from feedback import generate_feedback
from routes.resume import resume_bp
from routes.auth import auth_bp
from models.resume import db
import io

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# 🔧 Database Config (SQLite for now)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB with app
db.init_app(app)

# Register blueprints
app.register_blueprint(resume_bp)
app.register_blueprint(auth_bp)

# 🔍 Resume Grading Endpoint
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

# ✅ Ensure DB tables are created when starting
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
