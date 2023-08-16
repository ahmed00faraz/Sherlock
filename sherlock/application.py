from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class ReverseString(Resource):
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, string):
        if request.headers['api_key'] != self.api_key:
            return {'error': 'Invalid API key'}

        result_string = sherlock(string)

api.add_resource(ReverseString, '/sherlock/<string>', endpoint='sherlock_string')

if __name__ == '__main__':
    app.run(debug=True)
