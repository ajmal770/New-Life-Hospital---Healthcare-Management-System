import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hospital-management-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'instance', 'hospital.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
