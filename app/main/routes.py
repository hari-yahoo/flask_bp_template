from flask import render_template
from . import main_bp as main
from flask_login import login_required

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/about')
@login_required
def about():
    return render_template('about.html')
