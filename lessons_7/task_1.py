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

    def my_execute(self, sql, *args):
        cursor = self._conn.cursor()
        cursor.execute(sql, args)
        self._conn.commit()
        return cursor.fetchall()

    def my_select(self, sql, *args):
        cursor = self._conn.cursor()
        cursor.execute(sql, args)
        return cursor.fetchall()

    def __exit__(self, *args):
        self._conn.commit()
        self._conn.close()


if __name__ == '__main__':
    with ContexSqlManager('students.sqlite') as db:
        # print(db.my_execute('select * from student where first_name = "Igor"'))
        a = db.my_select('select id, group_name from student_group')
        for data in a:
            print(data)
