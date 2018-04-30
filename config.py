import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'QhDh7!sxk!vK2@&@JYJDKrV_hhSHMZ$N'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test'
