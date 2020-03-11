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

# list_of_threads = [Thread(target=time.sleep, args=(i,), name=f'name+{i}') for i in range(3)]
#
# for thread in list_of_threads:
#     thread.start()
#
# for thread in list_of_threads:
#     print(thread.is_alive())
#     print(thread.getName())
#     print(thread.setName(f'barab+{thread.getName()}'))
#     print(thread.getName())

a = []


def carculate(i):
    global a
    a.append(i)


list_of_threads = [Thread(target=carculate, args=(i,), name=f'name+{i}') for i in range(5)]

for thread in list_of_threads:
    thread.start()

time.sleep(1)

print(a)


class MyThread(Thread):

    def __init__(self, is_daemon):
        super().__init__(daemon=is_daemon)
        self.result = None
        self.is_runing = True

    def run(self):
        time.sleep(3)
        self.result = 3


a = MyThread(False)

a.start()

a.join()
print(a.result)
