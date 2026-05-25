import flask_login
from project.app import project
import dotenv, os
from user.models import User

dotenv.load_dotenv()
secret = os.getenv("SECRET")


login_manager = flask_login.LoginManager(app=project)
project.secret_key = secret

@login_manager.user_loader
def get_user(user_id):
    return User.query.get(user_id)