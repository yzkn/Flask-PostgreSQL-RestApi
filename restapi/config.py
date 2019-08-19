import os


class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{db}'.format(**{
        'user': os.getenv('DB_USER', 'userrestapi'),
        'password': os.getenv('DB_PASSWORD', 'Passw0rd'),
        'host': os.getenv('DB_HOST', 'localhost'),
        'db': os.getenv('DB_DATABASE', 'dbrestapi'),
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig