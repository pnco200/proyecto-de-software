class Config(object):
    """Base configuration,"""

    SECRET_KEY = "secret"
    TESTING = False
    SESSION_TYPE = "filesystem"
class ProductionConfig(Config):
    
    pass

class DevelopmentConfig(Config):
    """Development configuration."""
    DB_USER = "postgres"
    DB_PASS = "1234"
    DB_HOST = "localhost"
    DB_NAME = "CIDEPINT"
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