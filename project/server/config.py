# project/server/config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))
database_host = os.getenv('DB_HOST')
database_port = os.getenv('DB_PORT')
database_username = os.getenv('DB_USERNAME')
database_password = os.getenv('DB_PASSWORD')
postgres_local_base = 'postgresql://{}:{}@{}:{}/'.format(database_username, database_password, database_host, database_port)
database_name = os.getenv('DB_NAME')


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///example'
