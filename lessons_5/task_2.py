"""
Создать функцию, которая будет скачивать файл из интернета по ссылке, повесить на неё созданный декоратор.
Создать список из 10 ссылок, по которым будет происходить скачивание. Создать список потоков,
отдельный поток,на каждую из ссылок.
Каждый поток должен сигнализировать, о том, что, он начал работу и по какой ссылке он работает,
так же должен сообщать когда скачивание закончится.
"""

from threading import Thread
import requests

list_url = [
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-voda-15.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-32.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-lyudi-rasteniya-serdca-92.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-serdca-191.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-fon-336.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-fon-266.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-fon-174.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-steny-179.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-solnce-115.jpg',
    'https://mobimg.b-cdn.net/pic/v2/gallery/111x185/abstrakciya-127.jpg'

]

list_threads = []


def simple_decorator(name_thread, is_daemon):
    def actual_simple_decorator(func_to):
        def wrapper(*args):
            status_thread = Thread(target=func_to, args=(*args,), daemon=is_daemon, name=f'{name_thread}-{args[1]}')
            print(f'{status_thread.getName()} thread start download image {args[0]}')
            status_thread.start()
            list_threads.append(status_thread)

        return wrapper

    return actual_simple_decorator


@simple_decorator('my_thread', False)
def get_img(img_url, file_name):
    r = requests.get(url=img_url, allow_redirects=True)
    with open(f'{file_name}-image.jpg', 'wb') as file:
        file.write(r.content)


for id_, url in enumerate(list_url):
    get_img(url, str(id_))

status = True
while status:
    status = False
    for thread in list_threads:
        if thread.is_alive() is False:
            print(f'{thread.getName()} download complete')
            list_threads.remove(thread)
        else:
            status = True
