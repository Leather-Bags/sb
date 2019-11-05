import logging
import os
import types

from cmd import Cmd

__author__ = "Timur Israpilov"


class Console(Cmd):
    """Console for easy interactions with server. Allows to add custom commands.
    """

    # Magic methods
    def __init__(self, *, log: logging.Logger, config: dict, prefix: str = '> ', **kwargs):
        self.config = config
        self.log = log

        super().__init__()
        self.doc_leader = kwargs['doc_leader'] if 'doc_leader' in kwargs else 'Use ?<command> to see help\n'
        self.doc_header = kwargs['doc_header'] if 'doc_header' in kwargs else 'Commands with help'
        self.undoc_header = kwargs['undoc_header'] if 'undoc_header' in kwargs else 'Commands without help'
        self.ruler = kwargs['ruler'] if 'ruler' in kwargs else '-'
        self.prompt = prefix

    # Override methods
    def precmd(self, line: str) -> str:
        return line

    def default(self, line: str) -> None:
        self.stdout.write(f'Unknown command: {line}\n')

    def emptyline(self) -> None:
        ...

    def get_names(self) -> list:
        return list(set(dir(self) + list(self.__dict__)))

    # New methods
    def start(self, intro: str = '') -> None:
        self.log.info('Starting console')
        self.cmdloop(intro=f'{self.config["name"]} v{self.config["version"]}')

    def add_command(self, name: str, func, /, *, info: str = ''):
        self.__setattr__('do_' + name, func)
        if isinstance(info, types.FunctionType):
            self.__setattr__('help_' + name, info)
        elif isinstance(info, str):
            self.__setattr__('help_' + name, lambda: print(info))
        self.log.debug(f'Command "{name}" added{". With help info" if info else ""}')

    # Built-in commands
    def do_about(self, args: str) -> None:
        print(f'{self.config["name"]} v{self.config["version"]}')

    @staticmethod
    def help_about() -> None:
        print('Get info about server')

    @staticmethod
    def do_clear(args: str) -> None:
        os.system('clear' if os.name == 'posix' else 'cls')

    @staticmethod
    def help_clear() -> None:
        print('Clear terminal or CLI')

    @staticmethod
    def do_exit(args: str) -> bool:
        return True

    @staticmethod
    def help_exit() -> None:
        print('Exit from console')

    @staticmethod
    def do_shell(command: str) -> None:
        os.system(command)

    @staticmethod
    def help_shell() -> None:
        print('Start command in shell(terminal)\nUsage: !<command>')
