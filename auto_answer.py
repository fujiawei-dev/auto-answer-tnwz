import os
import shutil
from time import sleep

from cerium import AndroidDriver
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from constants import DIRECTORY, POSITION
from quizzes import insert_db
from utils import choose_parsing, confirm_question, question_parsing

shutil.rmtree(DIRECTORY)
os.mkdir(DIRECTORY)

driver = AndroidDriver(wireless=True)
# driver = AndroidDriver()
# driver.auto_connect()


class FileEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_created(self, event):
        global question, options
        if event.src_path.split('\\')[-1] == 'findQuiz':
            sleep(3)
            question, options = question_parsing()
            x, y = confirm_question(question, options)
            driver.click(x, y)
        elif event.src_path.split('\\')[-1] == 'choose':
            sleep(3)
            question, answer = choose_parsing(question, options)
            insert_db(question, answer)
        elif event.src_path.split('\\')[-1] == 'fightResult':
            print('游戏结束\n')
            sleep(1)
            driver.back()
            sleep(1)
            option = POSITION[-1]
            driver.swipe_up()
            driver.click(option['x'], option['y'])
            print('游戏开始')


if __name__ == "__main__":
    observer = Observer()
    handler = FileEventHandler()
    observer.schedule(handler, DIRECTORY, True)
    print('游戏开始')
    observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
