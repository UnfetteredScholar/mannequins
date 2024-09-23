from flask import jsonify, request

from app import db
from app.models.user import User
from app.routes import router


@router.route("/")
def index():
    return "This is The Main Blueprint"


@router.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = data["password"]

    user: User = User(
        username=username,
        email=email,
        password=password,
        sign_in_type="NORMAL",
        is_verified=True,
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "Register Success", "user_id": user.id})
