from uuid import uuid4

from sqlalchemy import TIMESTAMP, UUID, Boolean, Column, String, func

from app import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid4()))
    username = Column(String(120), unique=False, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), unique=False, nullable=False)
    sign_in_type = Column(String(20), unique=False, nullable=False)
    is_verified = Column(Boolean, unique=False, nullable=False, default=False)
    date_created = Column(
        TIMESTAMP, unique=False, nullable=False, default=func.now()
    )
    date_modified = Column(
        TIMESTAMP, unique=False, nullable=False, default=func.now()
    )
