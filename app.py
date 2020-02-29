from flask import Flask, jsonify
from flask_restful import Api, Resource
from gevent import pywsgi, monkey

from constant import bucket, access_key, secret_key, expired_time

monkey.patch_all()

app = Flask(__name__)

import qiniu

q = qiniu.Auth(access_key, secret_key)


class TokenHelper(Resource):
    def get(self):
        return jsonify(code=0, data={"token": q.upload_token(bucket=bucket, expires=expired_time)})


if __name__ == '__main__':
    api = Api(app)
    api.add_resource(TokenHelper, '/token')
    server = pywsgi.WSGIServer(('0.0.0.0', 5002), app)
    server.serve_forever()
