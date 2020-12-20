import os, os.path
import datetime
import logging

from backend.config.settings import LOGGING_DIR


class MyLogger:
    """
    Class For Handling Logging
    """

    def __init__(self, category):
        try:

            # Path
            self.category = category
            directory = LOGGING_DIR
            self.str_date = str(datetime.date.today()).replace('-', '_')
            file_path = os.path.join(directory, self.str_date + '.txt')
            if not os.path.exists(directory):
                os.makedirs(directory)

            # Logging Attributes
            self.logger = logging.getLogger(category)
            if not self.logger.hasHandlers():
                formatter = logging.Formatter('%(asctime)s,%(msecs)d | %(name)s | %(levelname)s | %(message)s')
                handler = logging.FileHandler(file_path, mode='a')
                handler.setFormatter(formatter)
                self.logger.setLevel(logging.INFO)
                self.logger.addHandler(handler)
            print('Logging Successful')

        except Exception:
            print('Logging Failure')
            raise

    def msg_logger(self, msg):
        # self.logger = logging.getLogger(self.category)
        self.logger.info('-' * 100)
        self.logger.info(msg)

    def error_logger(self, error, meta=''):
        # self.logger = logging.getLogger(self.category)
        self.logger.error('-' * 100)
        self.logger.error(error)
        if meta:
            self.logger.error(meta)
