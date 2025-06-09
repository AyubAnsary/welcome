from flask import render_template

from . import case_studies_bp


@case_studies_bp.route('/')
def index():
    return render_template('case_studies/index.html')


@case_studies_bp.route('/<slug>')
def single(slug):
    return render_template('case_studies/single.html', slug=slug)
