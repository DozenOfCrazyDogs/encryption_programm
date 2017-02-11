from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

module_one = Blueprint('simple_page', __name__,
                        template_folder='templates')

@module_one.route('/', defaults={'page': 'index'})
@module_one.route('/<page>')
def show(page):
    try:
        return render_template('module_one/%s.html' % page)
    except TemplateNotFound:
        abort(404)
