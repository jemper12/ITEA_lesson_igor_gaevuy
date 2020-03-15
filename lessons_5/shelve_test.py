import shelve

FILENAME = 'dbshelve.txt'


def create_user(id_, login, password):
    with shelve.open(FILENAME) as users:
        users[str(id_)] = (login, password)


def get_user(id_):
    with shelve.open(FILENAME) as file:
        return file.get(str(id_))


create_user(1, 'asd', 'ghgf')
print(get_user(1))
