import logging
import threading
from time import time

import config
from console import Console
from logger import Logger
from processing.db import Users

__author__ = "Timur Israpilov"

start_time = int(time())
logger = Logger(logging.getLevelName(config.log['level']))
console = Console(prefix=config.console['prefix'], log=logger.get_logger('console'), config=config,
                  start_time=start_time)
databases = {
    'users': Users()
}

if __name__ == "__main__":
    threads = {}

    log = logger.get_logger('core')
    log.info('Server starting')
    logger.console_integration(console)

    # Thread for console
    threads['console'] = threading.Thread(target=console.start)
    threads['console'].start()

    log.info('Server started')
