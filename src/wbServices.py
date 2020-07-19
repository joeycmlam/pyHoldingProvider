from flask import Flask
from flask_restful import Resource, Api


class api_root(Resource):
    def get(self):
        print('holdingProvider!')
        return {'src': 'version 0.0.1'}


if __name__ == '__main__':
    print ('test')
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(api_root, '/')

    app.run(host="0.0.0.0", port=int("80"), debug=True)