class Contex:
    def __init__(self, string):
        self._string = string

    def __enter__(self):
        return self

    def __exit__(self, *args):
        print(*args)
        print('Exit')
        self._string = self._string[::-1]


with Contex('qwerqwe') as string:
    print(string._string)
    string._string = 'qwe'
    print(string._string)


print(string._string)