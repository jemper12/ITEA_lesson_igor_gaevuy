"""
Создать декоратор с аргументами.
Который будет вызывать функцию, определенное кол-во раз,
    будет выводить кол-во времени затраченного на выполнение данной функции и её название.
"""
from time import time
from functools import wraps


def simple_decorator(arg1):
    def actual_simple_decorator(func_to):
        @wraps(func_to)
        def wrapper(args):
            func_result = func_to(args)
            for i in range(arg1):
                time_start_run = time()
                print(
                    f'{i + 1}) func {func_to.__name__} send message {func_result} on time {(time() - time_start_run)}'
                )
            return func_result

        return wrapper

    return actual_simple_decorator


@simple_decorator(15)
def func_fo_decorate(string):
    return string


func_fo_decorate('text fo massage')

print(f'func name in run = {func_fo_decorate.__name__}')
