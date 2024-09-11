from flask import Blueprint

# Define the Blueprint for the main module
main_bp = Blueprint('main_bp', __name__, template_folder='templates')

# Import the routes
from . import routes
