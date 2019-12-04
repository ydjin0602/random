import json
import logging
from flask import request, Flask
import random

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }

    handle_dialog(request.json, response)

    logging.info('Response: %r', response)
    return json.dumps(
        response,
        ensure_ascii=False,
        indent=2
    )


def handle_dialog(req, res):
    global x, y
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет, я рандомайзер) \n Задайте диапазон случайного числа (Х, Y). \n Веедите ' \
                                  'число X. '
        return

    count = 0
    if count == 0:
        if req['request']['original_utterance'].isdigit():
            x = int(req['request']['original_utterance'])
            res['response']['text'] = 'Введите число Y'
            count += 1
        else:
            res['response']['text'] = 'Это не похоже на число'


    if count == 1:
        if req['request']['original_utterance'].isdigit():
            y = int(req['request']['original_utterance'])
        else:
            res['response']['text'] = 'Это не похоже на число'

    res['response']['text'] = str(random.randint(x, y))
