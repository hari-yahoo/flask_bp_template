from . import api_bp as api


@api.route('/')
def home():
    return {'message': 'Welcome to the Flask API!'}