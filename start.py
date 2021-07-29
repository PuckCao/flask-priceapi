from flask import Flask
from flask_restful import Api, Resource

from app import app, bp


if __name__ == '__main__':
    app.run(debug=True,)

