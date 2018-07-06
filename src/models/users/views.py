from flask import Blueprint, render_template, request, session, redirect, url_for

import src.models.users.errors as Errors
from src.models.users.user import User

user_blueprint = Blueprint('buser', '__name__')


@user_blueprint.route('/')
def user():
    user=User.find_by_email(session['email'])
    return render_template('users/user.jinja2', user = user)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.login_is_valid(email, password) is True:
                session['email']=email
                user = User.find_by_email(email)
                return redirect(url_for('.user'))
        except Errors.UserDoesntExist:
            return "User doesnt exist"
        except Errors.PasswordIncorrect:
            return "Password Incorrect"
    return render_template('users/login.jinja2')


@user_blueprint.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            if User.register_is_valid(email):
                user = User(email=email, password=password)
                user.save_to_mongo()
                session['email'] = email
                return render_template('users/user.jinja2', user=user)
        except Errors.UserAlreadyRegistered:
            return "User already registered"

    return render_template('users/register.jinja2', value="Test variable", value2="Another test variable")


@user_blueprint.route('/logout')
def logout():
    session['email'] = None
    return render_template('home.jinja2')
