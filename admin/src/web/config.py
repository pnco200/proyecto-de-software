from os import environ 

class Config(object):
    """Base configuration,"""

    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem"
class ProductionConfig(Config):
      DB_USER = environ.get("DB_USER")
      DB_PASS = environ.get("DB_PASS")
      DB_HOST = environ.get("DB_HOST")
      DB_NAME = environ.get("DB_NAME")
      SQLALCHEMY_TRACK_MODIFICATIONS = True
      SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
       )


class DevelopmentConfig(Config):
    """Development configuration."""
    DB_USER = "postgres"
    DB_PASS = "ignacio"
    DB_HOST = "localhost"
    DB_NAME = "grupo25"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    )

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True


config = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}