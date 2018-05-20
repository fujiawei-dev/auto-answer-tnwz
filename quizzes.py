import sqlite3

from constants import QUIZZES


conn = sqlite3.connect(QUIZZES, check_same_thread=False)

def insert_db(question, answer):
    sql = "insert into quizzes(question, answer) values('%s', '%s')" % (question, answer)
    try:
        conn.execute(sql)
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    except sqlite3.OperationalError:
        print(sql, file=open('sql.log', 'a', encoding='utf-8'))


def match_question(question):
    question = question.strip('?').replace( "'", "\'").strip().replace('"', '\"')
    sql = 'select answer from quizzes where question="{}"'.format(question)
    answer = None
    try:
        cursor = conn.execute(sql).fetchone()
        if cursor:
            answer = cursor[0]
    except sqlite3.OperationalError:
        print(sql, file=open('sql.log', 'a', encoding='utf-8'))
    return answer


if __name__ == '__main__':
    question = '希腊神话中宙斯和阿波罗的关系是？'
    print(match_question(question))