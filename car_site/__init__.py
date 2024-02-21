from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from car_site.config import Config
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = '12345'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sxzibgup:uAqClw7daQjC3nzIcw0JNwnmg1OhVMz3@lallah.db.elephantsql.com/sxzibgup'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
app.config.from_object(Config)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from car_site import routes
from car_site import db