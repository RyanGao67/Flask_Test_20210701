from flask_restful import Resource, reqparse

class Test(Resource):
    def get(self, name):
        return {'message': name}, 200
