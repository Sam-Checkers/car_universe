from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from car_site.config import Config
from helpers import JSONEncoder
from car_site.models import db as root_db, login_manager, ma

app = Flask(__name__)
CORS(app)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
app.config.from_object(Config)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

from car_site import routes
from car_site import db