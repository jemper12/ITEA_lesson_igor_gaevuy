class MyStruct:

    def __init__(self, *args):
        self._contaier = [*args]

    def __getitem__(self, item):
        return self._contaier[item]

    def __setitem__(self, key, value):
        self._contaier[key] = value


a = MyStruct(1, 2, 3, 4, 5, 6)
print(a[3])


