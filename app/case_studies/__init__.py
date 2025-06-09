from flask import Blueprint

case_studies_bp = Blueprint('case_studies', __name__)

from . import routes  # noqa
