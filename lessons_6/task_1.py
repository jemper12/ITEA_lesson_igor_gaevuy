"""
Создать свою структуру данных Список, которая поддерживает индексацию. Методы pop, append, insert, remove, clear.
Перегрузить операцию сложения для списков, которая возвращает новый расширенный объект.
"""


class MyList:
    def __init__(self, *args):
        self._my_list = [*args]

    def append(self, item):
        self._my_list += [item]

    def pop(self, index=0):
        result = self._my_list[index]
        # self._my_list = [x for i, x in enumerate(self._my_list) if i != id_]
        self._my_list = self._my_list[0:index] + self._my_list[index + 1:len(self._my_list)]
        return result

    def __add__(self, other):
        a = MyList()
        a.list = self._my_list + other.list
        return a

    def insert(self, index, value):
        self._my_list = self._my_list[0:index] + [value] + self._my_list[index:len(self._my_list)]

    def remove(self, value):
        if value in self._my_list:
            for index, data in enumerate(self._my_list):
                if data == value:
                    self._my_list = self._my_list[0:index] + self._my_list[index + 1:len(self._my_list)]
                    break
        else:
            raise ValueError()

    def clear(self):
        self._my_list = MyList().list

    @property
    def list(self):
        return self._my_list

    @list.setter
    def list(self, value):
        self._my_list = value


my_list = MyList(5, 3, 8, 4, 8)
print(f'create list:\n{my_list.list}')

my_list.append(8)
print(f'append:\n {my_list.list}')

print(f'return pop:\n{my_list.pop(2)}')
print(f'pop:\n {my_list.list}')

my_list.insert(1, 23)
print(f'insert:\n {my_list.list}')

my_list.remove(8)
print(f'remove:\n {my_list.list}')

list_2 = MyList(3, 4, 5, 6, 2)
print(f'new obj list = {(my_list + list_2).list}')

my_list.clear()
print(f'clear:\n {my_list.list}')
