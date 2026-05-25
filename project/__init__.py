from .app import project
import user, chat
from .urls import *
from .db import *
from .login import *

project.register_blueprint(blueprint=user.user)
project.register_blueprint(blueprint=chat.chat)