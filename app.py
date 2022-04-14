import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity as identity_function
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList # sqlAlchemy needs this to create tables from the store.py file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db').replace("postgres://", "postgresql://", 1)
# this turns off Flask-SQLAlchemy's modification tracker, not SQLAlchemy's
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'josh'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/login' # optional code that changes /auth to /login ** MUST BE PLACED BEFORE requesting the JWT instance

jwt = JWT(app, authenticate, identity_function) # /auth

# optional include user's Id in the response in addition to access_token
# @jwt.auth_response_handler
# def customized_response_handler(access_token, identity):
#     return jsonify({
#         'access_token': access_token.decode('utf-8'),
#         'user_id': identity.id
#     })

# optional Flask-JWT raises JWTError when an error occurs within any of the handlers
# @jwt.error_handler
# def customized_error_handler(error):
#     return jsonify({
#         'message': error.description,
#         'code': error.status_code
#     }), error.status_code

# config JWT to expire within half hour
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

# config JWT auth key name to be 'email' instead of default 'username'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Rolf
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__': # if only this file is run as 'main' (not as import)
    db.init_app(app)
    app.run(port=5000, debug=True)
