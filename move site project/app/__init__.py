from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')

db = SQLAlchemy(app)
from .views import *
from .models import *

db.create_all()

manager = LoginManager(app)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
