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

person_list = []


class Person(ABC):

    def __init__(self, second_name, birthday, faculty):
        self._second_name = second_name
        self._age = datetime.now().year - datetime(birthday[0], birthday[1], birthday[2]).year
        self._faculty = faculty
        self._birthday = f'{birthday[0]}/{birthday[1]}/{birthday[2]}'

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
        a = f"""
second name = {self._second_name}
birthday = {self._birthday}
faculty = {self._faculty}"""
        return a

    @property
    def age(self):
        return self._age


class Student(Person):
    def __init__(self, second_name, birthday, faculty, course):
        super().__init__(second_name, birthday, faculty)
        self._course = course

    @property
    def info(self):
        a = f"""
second name = {self._second_name}
birthday = {self._birthday}
faculty = {self._faculty}
course = {self._course}
"""
        return a

    @property
    def age(self):
        return self._age


class Teacher(Person):
    def __init__(self, second_name, birthday, faculty, position, experience):
        super().__init__(second_name, birthday, faculty)
        self._position = position
        self._experience = experience

    @property
    def info(self):
        a = f"""
second name = {self._second_name}
birthday = {self._birthday}
faculty = {self._faculty}
position = {self._position}
experience = {self._experience}
"""
        return a

    @property
    def age(self):
        return self._age


person_list.append(Entrant('Gaevuy', (1994, 6, 7), 'Engine'))
person_list.append(Entrant('Galofastov', (1993, 4, 25), 'Engine'))
person_list.append(Student('Ivanov', (1990, 12, 12), 'Engine', 4))
person_list.append(Teacher('Golovan', (1975, 11, 19), 'Engine', 'teacher', 15))

for person in person_list:
    print(person.info)

print('search for a person with an age of 25 years')

for person in person_list:
    if 20 < person.age < 27:
        print(person.info, person.age)
