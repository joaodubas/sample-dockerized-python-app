# encoding: utf-8
import os


class Configuration(object):
    DATABASE = {
        'name': os.getenv('DB_NAME'),
        'engine': 'peewee.PostgresqlDatabase',
        'user': os.getenv('DB_USER'),
        'passwd': os.getenv('DB_PASS'),
    }
    DEBUG = bool(os.getenv('APP_DEBUG'))
    SECRET_KEY = os.getenv('APP_SECRET')
