from flask import Blueprint

router = Blueprint("routes", __name__)


from app.routes import login, register, user
