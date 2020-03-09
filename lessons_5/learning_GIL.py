################# Part 3 GIL

from threading import Thread
import time
from multiprocessing import Process


# def sleeping(time_to_sleep):
#     time.sleep(time_to_sleep)
#     print('I`v wake up!!!')
#
#
# sleeping(2)
# sleeping(3)
#
# t = Thread(target=sleeping, args=(2,))
# t2 = Thread(target=sleeping, args=(3,))
#
# start = time.time()
# t.start()
# t2.start()
# t.join()
# t2.join()

# print(time.time() - start)


def calculate(n):
    a = []
    for i in range(n):
        a.append(i)


start = time.time()
calculate(1000000)
calculate(1000000)

print(time.time() - start)

t = Process(target=calculate, args=(1000000,))
t2 = Process(target=calculate, args=(1000000,))

start = time.time()
t.start()
t2.start()
t.join()
t2.join()
print(time.time() - start)
