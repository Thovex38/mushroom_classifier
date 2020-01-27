"""App configuration."""
import os
#from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
#load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # # General
    # TESTING = os.getenv('TESTING')
    # DEBUG = os.getenv('DEBUG')
    # SECRET_KEY = os.getenv('SECRET_KEY')
    # # Database
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    # SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME')
    # FLASK_ENV = os.getenv('FLASK_ENV')
    # SQLALCHEMY_USERNAME = os.getenv('SQLALCHEMY_USERNAME ')
    # SQLALCHEMY_PASSWORD = os.getenv('SQLALCHEMY_PASSWORD')
    # SQLALCHEMY_DATABASE_NAME = os.getenv('SQLALCHEMY_DATABASE_NAME')
    # SQLALCHEMY_TABLE = os.getenv('SQLALCHEMY_TABLE')
    # SQLALCHEMY_DB_SCHEMA = os.getenv('SQLALCHEMY_DB_SCHEMA')
    # General Config
    TESTING = True
    DEBUG = True
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    SESSION_COOKIE_NAME = 'my_cookie'
    FLASK_ENV = 'prod'
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_USERNAME = 'admin'
    SQLALCHEMY_PASSWORD = 'password'
    SQLALCHEMY_DATABASE_NAME = 'mushroomdb'
    SQLALCHEMY_TABLE = 'passwords_table'
    SQLALCHEMY_DB_SCHEMA = 'public'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
