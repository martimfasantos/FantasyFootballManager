# controllers/auth_controller.py

from flask import Blueprint, redirect, render_template, request, flash, url_for
from ..services.auth_service import AuthService

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        password_conf = request.form.get('password-conf')

        if len(username) < 2:
            flash('Name must be greater than 1 character!', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters!', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters!', category='error')
        elif password != password_conf:
            flash('Passwords must match!', category='error')
        else:
            try:
                AuthService.register_user(email, username, password)
                flash('Account created!', category='success')
                return redirect(url_for('views.home'))
            except Exception as e:
                flash(str(e), category='error')
            return redirect(url_for('auth.register_user'))

    return render_template('register.html', user=AuthService.get_current_user())

@auth.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            AuthService.login_user(email, password)
            return render_template('home.html', user=AuthService.get_current_user())
        except Exception as e:
            flash(str(e), category='error')
            return redirect(url_for('auth.login_user'))
    else:
        return render_template('login.html', user=AuthService.get_current_user())

@auth.route('/logout', methods=['GET', 'POST'])
def logout_user():
    try:
        AuthService.logout_user()
        flash('User logged out!', category='success')
        return redirect(url_for('auth.login_user'))
    except Exception as e:
        flash(str(e), category='error')
