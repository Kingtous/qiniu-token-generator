import base64
import hmac
import json
import time
from hashlib import sha1

from constant import bucket, access_key, secret_key, expired_time


def get_token():
    data = {"scope": bucket}
    exp_time = int(time.time()) + expired_time
    data["deadline"] = exp_time
    s = json.JSONEncoder().encode(data).encode("utf-8")
    encoded = base64.b64encode(s)
    encoded_sign = base64.b64encode(hmac.new(secret_key.encode("utf-8"), encoded, sha1).digest()).decode("utf-8")
    return access_key + ":" + encoded_sign + ":" + encoded.decode("utf-8")


# 主函数
if __name__ == '__main__':
    print(get_token())
