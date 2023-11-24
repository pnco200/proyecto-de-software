from os import environ 

class Config(object):
    """Base configuration,"""

    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem"
class ProductionConfig(Config):
      GOOGLE_CLIENT_ID = '881883190578-vnnoublgbk6vkr5fk5akkotocn4tiohg.apps.googleusercontent.com'
      GOOGLE_CLIENT_SECRET = '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'
      GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")
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
    GOOGLE_CLIENT_ID = '881883190578-vnnoublgbk6vkr5fk5akkotocn4tiohg.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'
    GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")
    DB_USER = "postgres"
    DB_PASS = "43851110"
    DB_HOST = "localhost"
    DB_NAME = "prueba"
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