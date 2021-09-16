import os

class Config:
    '''
    General configuration parent class
    '''
    # NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/source?apiKey=a6c5c1049c834e5c81000fc6a5bddebc'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=a6c5c1049c834e5c81000fc6a5bddebc'

    NEWS_API_KEY= os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:melvin@localhost/watchlist'
    @staticmethod
    def init_app(app):
            pass
  




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}