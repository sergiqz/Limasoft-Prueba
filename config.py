import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:sergio1997@localhost/limasoftbd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
