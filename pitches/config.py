import os


class Config:
    """
    General configuration parent class
    """


class ProdConfig(Config):
    """
    Production configuration
    """


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}
