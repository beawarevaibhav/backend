from flask import Flask, request, jsonify
from flask_cors import CORS
from parser import extract_text_from_pdf, extract_sections
from scorer import score_resume
from feedback import generate_feedback
from routes.resume import resume_bp
from routes.auth import auth_bp
from models.resume import db
import io
import os  # <-- You were missing this import

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://frontend-two-gamma-69.vercel.app"}})


# 🔧 Database Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Register routes
app.register_blueprint(resume_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def home():
    return "Server is live!"

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

# ✅ Run the app with proper config for Render
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


