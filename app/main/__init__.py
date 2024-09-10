from flask import Blueprint

# Define the Blueprint for the main module
main = Blueprint('main', __name__, template_folder='templates')

# Import the routes
from . import routes
