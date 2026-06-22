import flask, flask_login
def render_chat():
    is_authenticated = flask_login.current_user.is_authenticated
    if not is_authenticated:
        return flask.redirect("/login")
    else:
        return flask.render_template("chat.html", is_authenticated=is_authenticated)
    # return flask.render_template("chat.html")