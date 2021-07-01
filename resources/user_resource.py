from flask_restful import Resource, reqparse
from flask import current_app
from dao.user import User
class UserResource(Resource):
    def get(self, name):
        print(name)
        result = User.find_by_username(name)
        if result:
            return {"message": "'user':{}, 'password':{}".format(result.username, result.password)}, 200
        else:
            return {"message": "Not found"}, 404

    def delete(self, name):
        result = User.delete_by_username(name)
        if result:
            return {"message": "Deleted {} users. ".format(result)}, 200
        else:
            return {"message": "User {} not found. ".format(name)}, 400

    parser_post = reqparse.RequestParser()
    parser_post.add_argument(
        'username',type=str,required=True,help="This field cannot be left blank!"
    )
    parser_post.add_argument(
        'password',type=str,required=True,help="This field cannot be left blank!"
    )
    def post(self):
        data = UserResource.parser_post.parse_args()
        username = data['username']
        password = data['password']
        if User.find_by_username(username):
            return {"message": "User with that username already exists. "}, 400
        result = User.create_by_username(username, password)
        if result:
            return {"message": "created {} users".format(result)}, 200
        else:
            return {"message": "User {} creation failed. ".format(username)}, 200

    def put(self):
        data = UserResource.parser_post.parse_args()
        username = data['username']
        password = data['password']
        if not User.find_by_username(username):
            return {"message": "User with that username does not exist. "}, 400
        result = User.update_by_username(username, password)
        if result:
            return {"message": "Successfully updated {} user password. ".format(result)}, 200
        else:
            return {"message": "Failed updating user password. "}, 200


