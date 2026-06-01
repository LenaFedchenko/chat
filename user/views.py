import flask
from .models import User
import werkzeug.security as security
from project.db import DATABASE
import flask_login
from .send_email import send_message

def render_register():
    if flask.request.method == "POST":
        email = flask.request.form["email"]
        password = flask.request.form["password"]
        if email and password:
            user_email = User.query.filter_by(email = email).first() 
            if not user_email:
                password_hash = security.generate_password_hash(password=password, salt_length=10)
                user = User(
                    email = email,
                    password = password_hash
                )
                DATABASE.session.add(user)
                DATABASE.session.commit()
                send_message(user.id, email)
                # return flask.redirect("/")

    return flask.render_template('register.html')


def render_login():
    if flask.request.method == "POST":
        email = flask.request.form["email"]
        password = flask.request.form["password"]
        if email and password:
            user = User.query.filter_by(email=email).first()
            is_password_compare = security.check_password_hash(user.password, password)
            if is_password_compare:
                flask_login.login_user(user=user)
                return flask.redirect("/")
    return flask.render_template("login.html")


def check_email():
    user_id = flask.request.args.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    if user != None:
        user.is_verify = True
        DATABASE.session.commit()
        flask_login.login_user(user)
        return flask.redirect("/")
