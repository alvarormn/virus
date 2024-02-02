from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://[user]:[password]@localhost/virus_game_db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
