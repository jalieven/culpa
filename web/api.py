from flask import Flask, request
from flask.ext.restful import Resource, Api

from jsonschema import Draft3Validator


class WebApi:
    def __init__(self, config):
        self.config = config
        self.app = Flask(__name__)
        self.api = Api(self.app)

        if self.config['enabled']:
            self.api.add_resource(BuildUrl, '/build/<string:build_key>')
            self.api.add_resource(EventStreamUrl, '/stream')

        if __name__ == "__main__":
            self.app.run()


class BuildUrl(Resource):

    build_schema = {
        "type": "object",
        "properties": {
            "key": {"type": "string"},
            "speak": {"type": "string"},
            "checkState": {"type": "boolean"},
            "checkTests": {"type": "boolean"}
        }
    }

    def get(self, build_key):
        # get some shit
        pass

    def put(self, build_key):
        build_data = request.data
        v = Draft3Validator(BuildUrl.build_schema)
        for error in sorted(v.iter_errors(build_data), key=str):
            print error
        #save some shit


class EventStreamUrl(Resource):

    def get(self):
        # get the stream
        pass

