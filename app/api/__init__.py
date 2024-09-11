from flask import Blueprint

# Define the Blueprint for the main module
api_bp = Blueprint('api_bp', __name__)

# Import the routes
from . import routes