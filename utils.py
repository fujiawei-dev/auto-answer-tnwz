import json
import os
import re

import grequests

from constants import (CLEAN_WORDS, DIR_CHOOSE, DIR_FINDQUIZ, HEADERS,
                       NEGATIVE_WORDS, POSITION)
from quizzes import match_question


usual = re.compile('[\u4e00-\u9fa5a-zA-Z0-9]+')


def choose_parsing(question, options):
    resp = json.load(open(DIR_CHOOSE, encoding='utf-8'))
    os.remove(DIR_CHOOSE)
    question = question.strip('?').replace("'", "\'").strip()
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
    urls = ('http://www.baidu.com/s?wd={}&pn={}&rn=50'.format(clean_question(question), i) for i in range(0, 201, 50))
    rs = (grequests.get(url, headers=HEADERS) for url in urls)
    responses = grequests.map(rs)
    counts = [0, 0, 0, 0]
    for response in responses:
        for i in range(4):
            counts[i] += response.text.count(options[i])
    option = counts.index(max(counts))
    for neg in NEGATIVE_WORDS:
        if neg in question:
            option = counts.index(min(counts))
            break
    return option


def clean_question(question):
    question = ''.join(usual.findall(question))
    for i in CLEAN_WORDS:
        question = question.replace(i, ' ')
    question = ' '.join(question.split())
    return question


def confirm_question(question, options):
    res = match_question(question)
    if res:
        try:
            option = options.index(res)
            print('数据库匹配成功')
        except ValueError:
            print('正在百度搜索中')
            option = search_question(clean_question(question), options)
    else:
        print('正在百度搜索中')
        option = search_question(question, options)
    position = POSITION[option]
    return position['x'], position['y']
