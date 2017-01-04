class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=1
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
