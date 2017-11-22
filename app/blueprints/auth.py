from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, url_for)
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash

from .. import db
from ..forms import LoginForm, RegistrationForm
from ..models.user import User
from ..utils.flash import flash_errors

auth = Blueprint('auth', __name__, template_folder='../templates/auth')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()

        if check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('misc.index'))
        else:
            flash('Unable to authorize your credentials')
            return form.redirect()
    else:
        flash_errors(form)
        return form.redirect()


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('misc.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if request.method == 'GET':
        return render_template('register.html', form=form)

    if form.validate_on_submit():
        user = User(form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)

        return redirect(url_for('misc.index'))
    else:
        flash_errors(form)
        render_template('register.html', form=form)
