import sqlite3

from constants import QUIZZES


conn = sqlite3.connect(QUIZZES, check_same_thread=False)

def insert_db(question, answer):
    sql = 'insert into quizzes(question, answer) values("%s", "%s")' % (question, answer)
    try:
        conn.execute(sql)
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    except sqlite3.OperationalError:
        print(sql, file=open('sql.log', 'a', encoding='utf-8'))


def match_question(question):
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
    question = "不属于莎士比亚的作品是？"
    answer = "'A Doll's House'"
    insert_db(question, answer)
    print(match_question(question))