from flask import Flask
from .main import main as main_blueprint
from .api import api as api_bp

def create_app():
    app = Flask(__name__)

    # Load the configuration settings
    app.config.from_object('config.Config')

    # Register the Blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
