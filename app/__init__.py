from flask import Flask

app = Flask(__name__, template_folder='../build', static_folder='../build/static')

from app import routes
