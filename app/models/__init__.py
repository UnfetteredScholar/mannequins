from .user import User


def init_db():
    from app import db

    db.create_all()
