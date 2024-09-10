from flask import Blueprint

# Define the Blueprint for the main module
api = Blueprint('api', __name__)

# Import the routes
from . import routes