from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE'] = 'sqlite:///cars.db'



migrate  =  Migrate(app,db)
#class  provided by  flask-migrate that  handles database migrations in flask
db.init_app(app)
# establishes the connectiona and configure the database object to work
# with flask application








if __name__ == '__main__':
    app.run(port=5555)