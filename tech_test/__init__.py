from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "databse.db"

def create_app(): 
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "fgdnjrkflefrfvj"
    # sqlachemy db stored at sqlite.. need to tell flask where it's located
    app.config["SQLAlchemy_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    # initialize db by giving it the flask app
    db.init_app(app)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    create_database(app)
    
    return app

def create_database(app):
    if not path.exists("tech_test/" + DB_NAME):
        db.create_all(app=app)
        print("created Database")
