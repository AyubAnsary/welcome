from flask import render_template

from . import blog_bp


@blog_bp.route('/')
def index():
    return render_template('blog/index.html')


@blog_bp.route('/<slug>')
def single(slug):
    return render_template('blog/single.html', slug=slug)
