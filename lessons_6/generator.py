"""
123
"""
import random


def random_generator(qnt_of_random_numbers):
    start = 0

    while start < qnt_of_random_numbers:
        start += 1
        yield random.randint(0, 100)


for i in random_generator(3):
    print(i)

iterator = iter(random_generator(3))
print(next(iterator))
print(next(iterator))
print(next(iterator))

randoms = [random.randint(0, 100) for x in range(10)]
print(randoms)
randoms = (random.randint(0, 100) for x in range(10))
print(randoms)

randoms = [(random.randint(0, 100), random.randint(0, 100)) for x in range(10)]
print(type(randoms))

randoms = {1: 5}
print(type(randoms))