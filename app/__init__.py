from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from app.config import Config
import os

db = SQLAlchemy()
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    csrf.init_app(app)

    with app.app_context():
        from app import models
        from app.routes import register_routes
        db.create_all()
        
        # Seed database on first run
        if models.Doctor.query.first() is None:
            doctors = [
                models.Doctor(name='Dr. John Smith', specialization='Cardiology'),
                models.Doctor(name='Dr. Emma Wilson', specialization='Neurology'),
                models.Doctor(name='Dr. David Brown', specialization='Orthopedics')
            ]
            db.session.bulk_save_objects(doctors)
            db.session.commit()
            
        register_routes(app)

    return app
