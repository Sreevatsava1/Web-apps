from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '8698246812740c293857a09'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
from flaskapp import routes
