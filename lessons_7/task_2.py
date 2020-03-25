"""
Создать базу данных студентов. У студента есть факультет, группа, оценки, номер студенческого билета.
Написать программу, с двумя ролями: Администратор, Пользователь.
Администратор может добавлять, изменять существующих студентов.
Пользователь может получать список отличников, список всех студентов, искать студентов по по номеру студенческого,
    получать полную информацию о конкретном студенте (включая оценки, факультет)
"""


class User:
    def __init__(self, username):
        self._username = username


class Admin(User):

    def add_new_student(self, faculty, group, student_id_number):
        pass

    @property
    def get_all_student(self):
        return

    @get_all_student.setter
    def get_all_student(self, student):

        pass

    @property
    def get_capability(self):
        return
