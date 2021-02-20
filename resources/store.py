from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'store': 'not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'store':'already exists'}, 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'store': 'deleted'}, 200 


class StoreList(Resource):
    def get(self):
        return {'stores': [s.json() for s in StoreModel.query.all()]}
