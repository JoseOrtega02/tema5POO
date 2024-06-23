from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()
def createApp():
    app= Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    with app.app_context():
        from .views import homeView
    return app