from flask import render_template

from . import services_bp


@services_bp.route('/')
def index():
    return render_template('services/index.html')


@services_bp.route('/<slug>')
def single(slug):
    return render_template('services/single.html', slug=slug)
