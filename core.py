import logging
from time import time

from yaml import safe_load

from console import Console
from logger import Logger

__author__ = "Timur Israpilov"

start_time = int(time())
config = safe_load(open('config.yml'))
logger = Logger(logging.getLevelName(config['log']['level']))
console = Console(prefix=config['console']['prefix'], log=logger.get_logger('console'), config=config,
                  start_time=start_time)

if __name__ == "__main__":
    log = logger.get_logger('core')
    log.info('Server starting')
    logger.console_integration(console)
    console.start()
    log.info('Server started')
