from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'

# Initialize the database
db.init_app(app)

# Perform database migrations
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=5555)
