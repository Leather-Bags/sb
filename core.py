import logging

from console import Console
from logger import Logger
from yaml import safe_load

__author__ = "Timur Israpilov"

config = safe_load(open('config.yml'))
logger = Logger(logging.getLevelName(config['log']['level']))
console = Console(prefix=config['console']['prefix'], log=logger.get_logger('console'), config=config)

if __name__ == "__main__":
    log = logger.get_logger('core')
    log.info('Server starting')
    log.info('Server started')
    console.start()
