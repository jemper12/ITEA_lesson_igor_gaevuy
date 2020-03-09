"""
Создать класс структуры данных Стек, Очередь.
"""
from collections import deque


class DataSteck:
    def __init__(self):
        self._steck = deque()

    def get_steck(self):
        return self._steck

    def add_item_to_steck(self, item):
        self._steck.append(item)

    def out_item_from_steck(self):
        if self._steck.__len__() > 0:
            return self._steck.popleft()
        else:
            return f'stack is empty'


class DataQueue:
    def __init__(self):
        self._queue = deque()

    def get_queue(self):
        return self._queue

    def add_item_to_queue(self, item):
        self._queue.append(item)

    def out_item_from_queue(self):
        if self._queue.__len__() > 0:
            return self._queue.pop()
        else:
            return f'queue is empty'


steck_ = DataSteck()

steck_.add_item_to_steck(1)
steck_.add_item_to_steck(2)
steck_.add_item_to_steck(3)
steck_.add_item_to_steck(4)

print(steck_.get_steck())

print(steck_.out_item_from_steck())
print(steck_.out_item_from_steck())
print(steck_.out_item_from_steck())
print(steck_.out_item_from_steck())
print(steck_.out_item_from_steck())

queue_ = DataQueue()

queue_.add_item_to_queue(1)
queue_.add_item_to_queue(2)
queue_.add_item_to_queue(3)
queue_.add_item_to_queue(4)

print(queue_.get_queue())

print(queue_.out_item_from_queue())
print(queue_.out_item_from_queue())
print(queue_.out_item_from_queue())
print(queue_.out_item_from_queue())
print(queue_.out_item_from_queue())
