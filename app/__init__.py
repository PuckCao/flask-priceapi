from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from app.views import Vegetable, Fruit
import pymongo

app = Flask(__name__)
bp = Blueprint('index',__name__)
api = Api(bp)
# db = SQLAlchemy(app)


app.register_blueprint(bp)
api.add_resource(Vegetable,'/vegetable')
api.add_resource(Fruit,'/fruit')
