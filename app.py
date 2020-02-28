from flask import Flask, jsonify
from flask_restful import *
import qiniu_util as qutil

app = Flask(__name__)


class TokenHelper(Resource):
    def get(self):
        return jsonify(token=qutil.get_token())


if __name__ == '__main__':
    api = Api(app)
    api.add_resource(TokenHelper, '/token')
    app.run(host="0.0.0.0", port=5002, debug=False, use_reloader=False)
