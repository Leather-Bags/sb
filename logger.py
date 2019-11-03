import logging
import os
import time

__author__ = "Timur Israpilov"


class Logger:
    """Server logging tool.
    """

    log_format = '[%(asctime)s %(levelname)s] [%(name)s] %(message)s'
    date = '%d-%m-%Y|%H:%M:%S'

    def __init__(self, level: int = logging.WARNING):
        if not os.path.exists('logs/'):
            os.makedirs('logs/')
        logging.basicConfig(filename=f'logs/{time.strftime("%d-%m-%Y-%H:%M:%S", time.localtime())}.log',
                            format=self.log_format,
                            datefmt=self.date,
                            level=level)
        self.log = logging.getLogger('logger')

    def change_level(self, level: int = logging.WARNING) -> None:
        self.log.info(
            f'Changing log level form {logging.getLevelName(logging.root.level)} to {logging.getLevelName(level)}')
        logging.root.setLevel(level)
        for i in logging.root.manager.loggerDict:
            logging.getLogger(i).setLevel(level)

    @staticmethod
    def get_logger(name: str = '') -> logging.Logger:
        return logging.getLogger(name)
