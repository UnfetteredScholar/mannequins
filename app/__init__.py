from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)
    app.url_map.strict_slashes = False

    # Extensions
    db.init_app(app)

    jwt = JWTManager(app)

    # Initialize db
    with app.app_context():
        from app.models import init_db

        init_db()

    # Blueprints
    from app.routes import router as main_router

    app.register_blueprint(main_router)

    @app.route("/test", methods=["GET"])
    def test():
        """Test route"""
        return "<h1>Testing the Flask Application Factory Pattern</h1>"

    return app
