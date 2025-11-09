from flask import Blueprint, render_template


allPdf_bp = Blueprint('allPdf', __name__, template_folder='template', url_prefix='/allpdf')

@allPdf_bp.route('/')
def index():
    return '<h1> raeched report generator <h1>'
