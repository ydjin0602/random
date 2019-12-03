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
    user_id = req['session']['user_id']
    if req['session']['new']:
        res['response']['text'] = 'Привет, я рандомайзер) \n Задайте диапазон случайного числа (Х, Y). \n Веедите ' \
                                  'число X. '

    if not req['request']['original_utterance'].isdigit():
        res['response']['text'] = 'Ошибка, введите еще раз'

    x = req['request']['original_utterance']

    res['response']['text'] = 'Веедите число Y.'

    y = req['request']['original_utterance']

    res['response']['text'] = random.randint(x, y)
