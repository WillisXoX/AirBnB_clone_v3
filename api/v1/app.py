#!/usr/bin/python3
'''
    app for registering blueprint and starting flask
'''
"""
    Setting environmental variables
"""
from os import getenv, environ
environ['HBNB_MYSQL_USER']   = 'hbnb_dev'
environ['HBNB_MYSQL_PWD']    = 'hbnb_dev_pwd'
environ['HBNB_MYSQL_HOST']   = 'localhost'
environ['HBNB_MYSQL_DB']     = 'hbnb_dev_db'
environ['HBNB_TYPE_STORAGE'] = 'db'
environ['HBNB_API_HOST']     = '0.0.0.0'
environ['HBNB_API_PORT']     = '5000'

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views




app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    '''
    close query after each session
    '''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    '''
    return JSON formatted 404 status code response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
