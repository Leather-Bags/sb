import logging
import os
import time

from console import Console

__author__ = "Timur Israpilov"


class Logger:
    """Server logging tool.
    """

    log_format = '[%(asctime)s %(levelname)s] [%(name)s] %(message)s'
    date = '%d-%m-%Y|%H:%M:%S'

    levels = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'FATAL']

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

    def get_logger(self, name: str = '') -> logging.Logger:
        self.log.debug(f'Gives logger "{name}"')
        return logging.getLogger(name)

    def console_integration(self, console: Console):
        self.log.info('Adding logger commands to console')

        def logger(args: str) -> None:
            args = args.split(' ') if len(args) else []
            try:
                if args[0] == "send":
                    if len(args) >= 2:
                        self.log.info(f"(from console) {' '.join(args[1:])}")
                        print(f"Message \n\"{' '.join(args[1:])}\"\nSent to log as INFO")
                    else:
                        print('No message to send.\nUsage: logger send <message>')
                elif args[0] == "level":
                    if len(args) == 1:
                        print(logging.getLevelName(logging.root.level))
                    else:
                        if args[1] in self.levels:
                            self.change_level(logging.getLevelName(args[1]))
                            print(f'Log level is {args[1]} now')
                        else:
                            print(f'Wrong level. Available levels: {self.levels}')
                else:
                    print(f'Argument "{args[0]}" not exists. Check ?logger')
            except IndexError:
                print('Not enough arguments. Check ?logger')

        console.add_command('logger', logger,
                            info='Command to interact with logger settings\nUsage: logger <argument>\nArguments:'
                                 '\n\tsend <message> - send message to log as INFO'
                                 '\n\tlevel <DEBUG/INFO/WARN/ERROR/FATAL> - change log level')
