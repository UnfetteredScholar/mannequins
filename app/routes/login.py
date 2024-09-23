import flask_bcrypt
from flask import jsonify, request
from flask_jwt_extended import create_access_token

from app.models.user import User
from app.routes import router


@router.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    print("Received data:", email, password)

    user: User = User.query.filter_by(email=email).first()

    if user and flask_bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(
            {"message": "Login Success", "access_token": access_token}
        )
    else:
        return jsonify({"message": "Login Failed"}), 401
