import logging
from time import time


import config
from console import Console
from logger import Logger

__author__ = "Timur Israpilov"

start_time = int(time())
logger = Logger(logging.getLevelName(config.log['level']))
console = Console(prefix=config.console['prefix'], log=logger.get_logger('console'), config=config,
                  start_time=start_time)

if __name__ == "__main__":
    log = logger.get_logger('core')
    log.info('Server starting')
    logger.console_integration(console)
    console.start()
    log.info('Server started')
