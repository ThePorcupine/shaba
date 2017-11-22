from flask import Blueprint, render_template

auth = Blueprint('auth', __name__, template_folder='../templates/auth')

@auth.route('/login')
def login():
    return 'hey'

@auth.route('/register')
def register():
    return 'register'
