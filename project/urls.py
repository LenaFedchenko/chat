import user, chat


user.user.add_url_rule(
    rule = '/register/',
    view_func = user.render_register,
    methods = ["GET", "POST"]
)

chat.chat.add_url_rule(
    rule = '/',
    view_func = chat.render_chat,
    methods = ["GET", "POST"]
)

user.user.add_url_rule(
    rule = '/login/',
    view_func = user.render_login,
    methods = ["GET", "POST"]
)
user.user.add_url_rule(
    rule = '/check_email/',
    view_func = user.check_email,
    methods = ["GET", "POST"]
)
user.user.add_url_rule(
    rule = '/get_data/',
    view_func = user.get_data,
    methods = ["POST"]
)