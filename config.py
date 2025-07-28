import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:furgofinder@db-furgofinder.czmmeo2ky6di.us-east-2.rds.amazonaws.com:3306/furgofinder'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


