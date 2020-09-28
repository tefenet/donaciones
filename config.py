from os import environ


class BaseConfig(object):
    """Base configuration."""

    DEBUG = False
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_NAME = environ.get("DB_NAME")
    SECRET_KEY = "grupo56_dev"
    SQLALCHEMY_URI = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    ENV = "development"
    DEBUG = environ.get("DEBUG", True)


class TestingConfig(BaseConfig):
    """Testing configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = environ.get("DEBUG", True)
    DB_NAME = environ.get("DB_NAME", "grupo56_test")
    SQLALCHEMY_URI = 'mysql://{}:{}@{}/{}'.format(BaseConfig.DB_USER, BaseConfig.DB_PASS, BaseConfig.DB_HOST, DB_NAME)


class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENV = "production"
    DEBUG = environ.get("DEBUG", False)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "grupo56")
    DB_PASS = environ.get("DB_PASS", "MWQ3MzkxOTQwYWMw")
    DB_NAME = environ.get("DB_NAME", "grupo56")
    SQLALCHEMY_URI = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASS, DB_HOST, DB_NAME)


config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
