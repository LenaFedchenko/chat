from .app import project
from .socket import socketio
import user, chat
from .urls import *
from .db import *
from .login import *
from .loadenv import execute


project.register_blueprint(blueprint=user.user)
project.register_blueprint(blueprint=chat.chat)
socketio.init_app(project)
