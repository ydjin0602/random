import json
from flask import request, Flask
import random
import re

NUM_REGEXP = '\-?[0-9]+(\.[0-9]+)?'
NUM_REGEXP_COMPILED = re.compile(NUM_REGEXP)

app = Flask(__name__)


@app.route("/", methods=['POST'])
def handle_random():
    req_body = request.json

    if not __is_body_valid(req_body):
        return json.dumps(
            {'message': 'invalid request body'}
        ), 400

    a = int(req_body['a'])
    b = int(req_body['b'])
    rand_num = random.randint(a, b)

    return json.dumps(rand_num)


def __is_body_valid(req_body) -> bool:
    a_ok = __is_number(req_body['a'])
    b_ok = __is_number(req_body['b'])

    return 'a' in req_body and 'b' in req_body and a_ok and b_ok


def __is_number(num) -> bool:
    return NUM_REGEXP_COMPILED.fullmatch(num) is not None


if __name__ == '__main__':
    app.run()
