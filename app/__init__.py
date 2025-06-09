from flask import Flask


def create_app():
    app = Flask(__name__)

    from .main.routes import main_bp
    from .blog.routes import blog_bp
    from .case_studies.routes import case_studies_bp
    from .services.routes import services_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(blog_bp, url_prefix='/blogs')
    app.register_blueprint(case_studies_bp, url_prefix='/case-studies')
    app.register_blueprint(services_bp, url_prefix='/services')

    return app
