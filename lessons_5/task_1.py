"""
Создать декоратор, который будет запускать функцию в отдельном потоке.
Декоратор должен принимать следующие аргументы:
    1) название потока
    2) является ли поток демоном
"""

from threading import Thread


def simple_decorator(name_thread, is_daemon):
    def actual_simple_decorator(func_to):
        def wrapper(*args):
            status_thread = Thread(target=func_to, args=(*args,), daemon=is_daemon, name=name_thread)
            status_thread.start()
            print(f'\nis thread = {status_thread.is_alive()}\n'
                  f'is daemon = {status_thread.isDaemon()}\n'
                  f'name = {status_thread.getName()}')

        return wrapper

    return actual_simple_decorator


@simple_decorator('my_thread', False)
def printing(text):
    print(text)


printing('Hello World')
