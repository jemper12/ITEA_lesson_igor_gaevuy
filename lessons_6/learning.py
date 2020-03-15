"""
lessons 6
"""
import random
import itertools


iterbl = [2, 5, 3, 4, 6, 3, 4]

iterator = iter(iterbl)


# print(iterator)
# print(next(iterator))


class RandomGeneratorIterator:
    def __init__(self, random_generator_instance):
        self._instance = random_generator_instance
        self._instance._start = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self._instance._start < self._instance._quantity:
            self._instance._start += 1
            return random.randint(0, 100)
        else:
            raise StopIteration('End')


class RandomGenerator:
    def __init__(self, quantity_of_random):
        self._quantity = quantity_of_random
        self._start = 0

    def __iter__(self):
        return RandomGeneratorIterator(self)


range_ = RandomGenerator(4)
for i in range_:
    print(i)
    for j in range_:
        print(i, j)
