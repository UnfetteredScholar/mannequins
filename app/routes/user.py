from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.models.user import User
from app.routes import router


@router.route("/users/me", methods=["GET"])
@jwt_required()
def get_name():
    # Extract the user ID from the JWT
    user_id = get_jwt_identity()
    user: User = User.query.filter_by(id=user_id).first()

    # Check if user exists
    if user:
        return jsonify({"message": "User found", "name": user.username})
    else:
        return jsonify({"message": "User not found"}), 404
