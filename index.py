from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')

version = ""


@bp.route('/')
def index():
    return render_template('index.html', version=version)