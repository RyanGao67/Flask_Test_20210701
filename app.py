from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# add root path so that dao.user is valid in resources.user_resource
import sys
sys.path.append('.')

def create_app(config):
    # instance_relative_config will allow the app to look for config in ./instance/
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config)
    # user auth
    from werkzeug.security import safe_str_cmp
    from dao.user import User
    def authenticate(username, password):
        user = User.find_by_username(username)
        if user and safe_str_cmp(user.password, password):
            return user
    def identity(payload):
        user_id = payload['identity']
        return User.find_by_id(user_id)
    jwt = JWT(app, authenticate, identity)

    # resources
    api = Api(app)
    from resources.test import Test
    from resources.user_resource import UserResource
    api.add_resource(Test, '/test/<string:name>')
    api.add_resource(UserResource, '/user', '/user/<string:name>')
    return app

if __name__ == '__main__':
    # create app and api
    app = create_app('config.py')
    app.run(debug=True)
