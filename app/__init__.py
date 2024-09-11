from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .main import main_bp
from .api import api_bp



db = SQLAlchemy()
login_manager = LoginManager()
from .models import User

def create_app():
    app = Flask(__name__)

    # Load the configuration settings
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    # Set the login view (the page where users are redirected if they're not logged in)
    login_manager.login_view = 'auth_bp.login'

    # User loader callback for Flask-Login
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  # Load the user from the database

    from .auth import auth_bp
    # Register the Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
