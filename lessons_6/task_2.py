"""
Создать свою структуру данных Словарь, которая поддерживает методы, get, items, keys, values.
Так же перегрузить операцию сложения для словарей, которая возвращает новый расширенный объект.
"""


class MyDict:

    def __init__(self, *kwargs):
        self._my_dict = dict(*kwargs)

    def get(self, value):
        if value in self.get_dict:
            return self.get_dict[value]
        else:
            return None

    def items(self):
        list_to_return = []
        for key in self.get_dict:
            list_to_return.append((key, self.get_dict[key]))
        return list_to_return

    def keys(self):
        list_to_return = []
        for key in self.get_dict:
            list_to_return.append(key)
        return list_to_return

    def __add__(self, other):
        a = MyDict(self.get_dict)
        for key, value in other.items():
            a.get_dict.update({key: value})
        return a.get_dict

    def values(self):
        list_to_return = []
        for key in self.get_dict:
            list_to_return.append(self.get_dict[key])
        return list_to_return

    @property
    def get_dict(self):
        return self._my_dict

    @get_dict.setter
    def get_dict(self, value):
        self._my_dict = value


my_dict = MyDict({'Igor': 'Gaevuy', 'Yaroslav': 'Obichod', 'Nikolay': 'Universal'})
print(f'create dict:\n{my_dict.get_dict}')

print(f'get Igor in dict:\n{my_dict.get("Igor")}')

print(f'items in dict\n{my_dict.items()}')

print(f'keys in dict\n{my_dict.keys()}')

print(f'values in dict\n{my_dict.values()}')

my_dict_2 = MyDict({'Olha': 'Ivanova'})

print(f'add 2 dict\n{my_dict + my_dict_2}')
