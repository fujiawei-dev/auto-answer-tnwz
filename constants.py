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
    # {'x': 500, 'y': 1050},   # begin
    # {'x': 500, 'y': 1500},
    {'x': 500, 'y': 1800},
]


NEGATIVE_WORDS = ['不是', '不属于', '不包括', '不正确', '未在', '没有', '未']
CLEAN_WORDS = ['选项中', '有关', '时常用', '以下', '想去', '应该', '去哪里', '哪里', '我国古代', '下面', '最有可能', '下列', '唱的是', '哪句话', '由谁', '谁', '哪个地方', '哪个', '哪一个', '哪一种', '哪位', '哪种', '哪部', '哪座', '哪只', '哪首', '与', '不同', '不在', '哪项',
               '什么', '不是', '就是', '不是指', '是指', '指的是', '是', '的', '没有', '有', '很多', '中不包括', '不属于', '属于', '不包括', '不正确', '未在', '通常', '著名', '诗句', '哪首诗', '请问', '什么东西', '选项', '呢', '具有', '哪本书', '还', '这种', '之一', '常用', '我们']
