from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix = '/')


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('board/board_list.html')
