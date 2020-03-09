"""
Создайте класс ПЕРСОНА с абстрактными методами, позволяющими вывести на экран информацию о персоне,
а также определить ее возраст (в текущем году).
Создайте дочерние классы:
    АБИТУРИЕНТ (фамилия, дата рождения, факультет),
    СТУДЕНТ (фамилия, дата рождения, факультет, курс),
    ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
        со своими методами вывода информации на экран и определения возраста.

Создайте список из n персон, выведите полную информацию из базы на экран,
а также организуйте поиск персон, чей возраст попадает в заданный диапазон.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Person(ABC):

    def __init__(self, second_name, birthday, faculty):
        self._second_name = second_name
        self._birthday = datetime.now().year - datetime(birthday[0], birthday[1], birthday[2])
        self._faculty = faculty

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def age(self):
        pass


class Entrant(Person):
    def __init__(self, second_name, birthday, faculty):
        super().__init__(second_name, birthday, faculty)

    @property
    def info(self):
        return self._second_name

    @property
    def age(self):
        return self._birthday


person1 = Entrant('Gaevuy', (1994, 11, 12), 'Engine')

print(person1.info)
print(person1.age)
