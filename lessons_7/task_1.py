"""
Написать контекстный менеджер для работы с SQLite DB.
"""

import sqlite3


class ContexSqlManager:
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        self._conn = sqlite3.connect(self._name)
        return self

    def my_execute(self, sql):
        cursor = self._conn.cursor()
        cursor.execute(sql)
        self._conn.commit()

    def my_select(self, sql):
        cursor = self._conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def __exit__(self, *args):
        self._conn.commit()
        self._conn.close()


with ContexSqlManager('identifier.sqlite') as db:
    print(db.my_select('select * from employee'))
