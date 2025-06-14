from flask import Blueprint, request, jsonify
from models.user import db, User
import jwt
import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
SECRET_KEY = "supersecretkey"  # 🔐 Store this securely

# Register new user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Login and return JWT token
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }, SECRET_KEY, algorithm='HS256')
        return jsonify({"token": token})
    else:
        return jsonify({"error": "Invalid credentials"}), 401
