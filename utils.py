import json
import os
import os.path
from time import sleep

import grequests

from constants import (DIR_CHOOSE, DIR_FINDQUIZ, HEADERS, NEGATIVE_WORDS,
                       POSITION)
from quizzes import match_question


def choose_parsing(question, options):
    resp = json.load(open(DIR_CHOOSE, encoding='utf-8'))
    os.remove(DIR_CHOOSE)
    question = question.strip('?').replace("'", "\'").strip().replace('"', '\"')
    option = int(resp['data']['answer']) - 1
    answer = options[option]
    return question, answer


def question_parsing():
    resp = json.load(open(DIR_FINDQUIZ, encoding='utf-8'))
    os.remove(DIR_FINDQUIZ)
    question = resp['data']['quiz']
    options = resp['data']['options']
    return question, options


def search_question(question, options):
    urls = ('http://www.baidu.com/s?wd={}&pn={}&rn=50'.format(question, i) for i in range(0, 201, 50))
    rs = (grequests.get(url, headers=HEADERS) for url in urls)
    responses = grequests.map(rs)
    counts = [0, 0, 0, 0]
    for response in responses:
        for i in range(4):
            counts[i] += response.text.lower().count(options[i])
    option = counts.index(max(counts))
    for neg in NEGATIVE_WORDS:
        if neg in question:
            option = counts.index(min(counts))
            break
    return option


def confirm_question(question, options):
    res = match_question(question)
    if res:
        while not os.path.exists(DIR_CHOOSE):
            option = options.index(res)
            sleep(0.5)
    else:
        option = search_question(question, options)
    position = POSITION[option]
    return position['x'], position['y']