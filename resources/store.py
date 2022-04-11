from flask_restful import Resource #, reqparse
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404 # not found

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400 # something wrong with request

        store = StoreModel(name) # data['price'], data['store_id'])
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500 # 500: internal server error

        return store.json(), 201 # created
        # the reason for adding .json() is because it needs to return a JSON dictionary, not an object

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        else:
            return {'message': 'Store does not exist to delete'}

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [x.json() for x in StoreModel.query.all()]}
