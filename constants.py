DIRECTORY = 'D:/Data Analysis/Charles Mirror/question-zh.hortor.net/question/bat'
DIR_CHOOSE = DIRECTORY + '/choose'
DIR_FINDQUIZ = DIRECTORY + '/findQuiz'

QUIZZES = 'quizzes.db'

HEADERS = {
    'Host': 'www.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
}

POSITION = [
    {'x': 540, 'y': 1000},
    {'x': 540, 'y': 1200},
    {'x': 540, 'y': 1380},
    {'x': 540, 'y': 1580},
    # {'x': 500, 'y': 800},
    # {'x': 500, 'y': 1000},
    {'x': 500, 'y': 1050},   # begin
]


NEGATIVE_WORDS = ['不是', '不属于', '不包括', '不正确', '未在']