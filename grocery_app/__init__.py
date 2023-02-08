from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from grocery_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from grocery_app.routes import main

app.register_blueprint(main)

with app.app_context:
    db.create_all()