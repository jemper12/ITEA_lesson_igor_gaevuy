"""
new_exp
"""


class Point:
    """
    asdkalsdklaskdlaksdlksald
    """
    _instances = None

    def __new__(cls, *args, **kwargs):
        """1234567890alasdasdlsd"""
        if cls._instances:
            raise Exception('It`s a singletone type')
        else:
            cls._instances = super().__new__(cls)
            return cls._instances


a = Point()
a.x = 100


class UsefullMethods:
    def make_class_feel_good(self):
        print('Feeling good')


class MyMetta(type):
    def __new__(mcls, name, bases, attributes):
        if '_' in name:
            raise NameError('U can`d name class')
        bases += (UsefullMethods, object)
        print(mcls,name, bases, attributes)
        return super().__new__(mcls, name, bases, attributes)


class Point(metaclass=MyMetta):
    name = 'PointClass'

    def __init__(self, x):
        self.x = x


print(Point.__bases__)
