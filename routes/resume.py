# routes/resume.py

from flask import Blueprint, request, jsonify
from models.resume import db, Resume
from flask_jwt_extended import jwt_required, get_jwt_identity

resume_bp = Blueprint('resume', __name__, url_prefix='/api/resumes')

@resume_bp.route('/', methods=['POST'])
@jwt_required()
def save_resume():
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data or 'content' not in data:
        return jsonify({"error": "Missing resume content"}), 400

    resume = Resume(user_id=user_id, content=data['content'])
    db.session.add(resume)
    db.session.commit()

    return jsonify({"message": "Resume saved", "resume": resume.to_dict()}), 201

@resume_bp.route('/', methods=['GET'])
@jwt_required()
def get_user_resumes():
    user_id = get_jwt_identity()
    resumes = Resume.query.filter_by(user_id=user_id).order_by(Resume.created_at.desc()).all()
    return jsonify([r.to_dict() for r in resumes]), 200
