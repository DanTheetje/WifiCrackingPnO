from flask import Blueprint, render_template

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return render_template('index.html')
