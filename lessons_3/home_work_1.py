"""
Создать класс структуры данных Стек, Очередь.
"""
from collections import deque


class DataStructures:
    def __init__(self):
        self._deque = deque()

    def get_deque(self):
        return self._deque

    def add_item_to_deque(self):
        print('add elements to deque')
        list_ = ['Igor', 'Andrey', 'Ivan', 'Katya', 'Konstantyn']
        for i in range(list_.__len__()):
            print(f'\t{i + 1}) add {list_[i]}')
            self._deque.append(list_[i])

    def out_all_as_fifo(self):
        print('Out all elements as fifo:')
        for i in range(self._deque.__len__()):
            print(f'\t{i + 1}) {self._deque.popleft()}')

    def out_all_as_lifo(self):
        print('Out all elements as lifo:')
        for i in range(self._deque.__len__()):
            print(f'\t{i + 1}) {self._deque.pop()}')


init_deque = DataStructures()

init_deque.add_item_to_deque()
print(f'in {init_deque.get_deque()}')
init_deque.out_all_as_fifo()
print(f'in {init_deque.get_deque()}\n')

init_deque.add_item_to_deque()
print(f'in {init_deque.get_deque()}')
init_deque.out_all_as_lifo()
print(f'in {init_deque.get_deque()}\n')
