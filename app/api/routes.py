from . import api


@api.route('/')
def home():
    return {'message': 'Welcome to the Flask API!'}