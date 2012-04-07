class development(object):
    DEBUG = True
    TESTING = False

    SECRET_KEY = 'development'

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'quincy-development'
    MONGO_USERNAME = None
    MONGO_PASSWORD = None


class testing(object):
    DEBUG = False
    TESTING = True

    SECRET_KEY = 'testing'

    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_DBNAME = 'quincy-testing'
    MONGO_USERNAME = None
    MONGO_PASSWORD = None


class production(object):
    DEBUG = False
    TESTING = False

