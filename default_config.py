import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get("PROD_DATABASE_URL", "DEV_DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
PROPAGATE_EXCEPTIONS = True
APP_SECRET_KEY = 'iamdoingwell'
