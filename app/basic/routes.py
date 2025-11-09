from flask import Blueprint, render_template

basic_bp = Blueprint('basic', __name__, template_folder='templates')

@basic_bp.route('/')
def home():
    return render_template('index.html')

@basic_bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')