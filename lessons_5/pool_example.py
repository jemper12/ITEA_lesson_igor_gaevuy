from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from time import sleep
from concurrent.futures import as_completed

executor = ProcessPoolExecutor(max_workers=100)


def sleeping(time_to_sleep):
    sleep(time_to_sleep)
    return time_to_sleep


a = executor.submit(sleeping, 1)
print(a.result())

a = []
for i in range(10):
    a.append(executor.submit(sleeping, i))

for result_future in as_completed(a):
    print(result_future.result())
