import os

import config

__author__ = 'Timur Israpilov'


def check_data(create: bool = True) -> bool:  # Check for /data
    if os.path.exists(f'{config.data}/data'):
        return True
    else:
        os.makedirs(f'{config.data}/data') if create else None
        return False


def check_clients(create: bool = True) -> bool:  # Check for /data/clients
    if os.path.exists(f'{config.data}/data/clients'):
        return True
    else:
        os.makedirs(f'{config.data}/data/clients') if create else None
        return False


def check_employees(create: bool = True) -> bool:  # Check for /data/employees
    if os.path.exists(f'{config.data}/data/employees'):
        return True
    else:
        os.makedirs(f'{config.data}/data/employees') if create else None
        return False


def check_users_db(create: bool = True) -> bool:  # Check for /data/users.db
    if os.path.isfile(f'{config.data}/data/users.db'):
        return True
    else:
        open(f'{config.data}/data/users.db', 'w+') if create else None
        return False


def check_all():
    check_data()
    check_clients()
    check_employees()
    check_users_db()
