from flask import Blueprint, render_template
from flask_login import login_required

misc = Blueprint('misc', __name__)


@misc.route('/')
def index():
    return render_template('index.html')


@misc.route('/loginreq')
@login_required
def loginreq():
    return 'i am logged in'
