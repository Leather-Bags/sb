from sqlite3 import connect

from sqlite_utils.db import Database, Table

import config

__author__ = 'Timur Irapilov'


class Clients(Table):
    """
    Class for work with Clients table
    """

    def __init__(self, db):
        super().__init__(db, 'clients')
        if not self.exists:
            self.create({
                'id': int,
                'login': str,
                'password': str,
                'email': str,
                'birthday': int,
                'first_name': str,
                'middle_name': str,
                'second_name': str,
                'passport': int
            }, pk='id',
                column_order=(
                    'id',
                    'login',
                    'password',
                    'email',
                    'birthday',
                    'first_name',
                    'second_name',
                    'middle_name',
                    'password'
                ),
                not_null={'id', 'login', 'password', 'email', 'birthday', 'first_name', 'second_name'}
            )
            self.create_index(['id'], unique=True)
            self.create_index(['login'], unique=True)
            self.create_index(['email'], unique=True)
            self.create_index(['passport'], unique=True)


class Users:
    """
    Abstract class for work with Clients and Employees in users.db
    """

    def __init__(self):
        self.connection = Database(connect(f'{config.data}/data/users.db'))
        self.clients = Clients(self.connection)  # Clients table

    def create_client(
            self,
            login: str,
            password: str,
            email: str,
            birthday: int,
            first_name: str,
            second_name: str,
            middle_name: str = ''
    ):
        self.clients.insert({
            'login': login,
            'password': password,
            'email': email,
            'birthday': birthday,
            'first_name': first_name,
            'second_name': second_name,
            'middle_name': middle_name,
        })
