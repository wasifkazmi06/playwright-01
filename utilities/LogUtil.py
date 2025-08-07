import logging
import os
import time


class Logger():

    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        curr_time = time.strftime("%Y-%m-%d")
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Directory where configReader.py is located
        LOG_PATH = os.path.join(BASE_DIR, "..", "logs", "log")  # Navigate to conf.ini

        # self.LogFileName = 'Logs\\log' + curr_time + '.txt'
        self.LogFileName = LOG_PATH + curr_time + '.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
