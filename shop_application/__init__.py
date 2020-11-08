from flask import Flask

from flask_migrate import Migrate

from shop_application.config import Config
from shop_application.models import db


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app=app, db=db)

from shop_application.views import *
