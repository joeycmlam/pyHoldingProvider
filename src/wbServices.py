from flask import Flask
from flask_restful import Resource, Api
import positionProvider


class api_root(Resource):
    def get(self):
        print('holdingProvider!')
        return {'src': 'version 0.0.1'}


class api_holding(Resource):
    def get(self):
        try:
            p = positionProvider.Position()
            h = p.getHolding()
            result = p.getHoldingJosn()
        except (Exception) as err:
            print(err)

        return result

def main():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(api_root, '/')
    api.add_resource(api_holding, '/holdings')
    app.run(host="0.0.0.0", port=int("80"), debug=True)

if __name__ == '__main__':

    print ('test')
    main()
