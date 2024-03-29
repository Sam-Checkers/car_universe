from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from car_site.config import Config
from car_site.models import db as root_db, login_manager, ma

app = Flask(__name__)
CORS(app)

bcrypt = Bcrypt(app)
app.config.from_object(Config)

app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

from car_site import routes