"""
Создать класс точки, реализовать конструктор который инициализирует 3 координаты (x, y, z).
Реалзиовать методы для получения и изменения каждой из координат.
Перегрузить для этого класса методы сложения, вычитания, деления, умножения.
Перегрузить один любой унарный метод.

Ожидаемый результат:
    умножаю точку с координатами 1,2,3 на другую точку с такими же координатами, получаю результат 1, 4, 9.
"""


class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    """Сложение"""

    def __add__(self, other):
        return Point(self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())

    """Отнимание"""

    def __sub__(self, other):
        return Point(self._x - other.get_x(), self._y - other.get_y(), self._z - other.get_z())

    """Умножение"""

    def __mul__(self, other):
        return Point(self._x * other.get_x(), self._y * other.get_y(), self._z * other.get_z())

    """Деление"""

    def __truediv__(self, other):
        if other.get_x() and other.get_y() and other.get_z():
            return Point(self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())
        else:
            print(f'Error, ZeroDivisionError{other.get_x(), other.get_y(), other.get_z()}, so new Point x=0 y=0 z=0 ')
            return Point(0, 0, 0)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, to):
        self._x = to

    def set_y(self, to):
        self._y = to

    def set_z(self, to):
        self._z = to

    # Only fo me
    def get_all_point_this(self):
        a = f'x={self._x} y={self._y}, z={self._z}'
        return a


point_1 = Point(5, 2, 6)
point_2 = Point(1, 1, 1)
point_3 = point_1 + point_2
print(f'Result after add method {point_3.get_all_point_this()}')

print(f'Result after sub method {(point_1 - point_2).get_all_point_this()}')

point_4 = Point(0, 4, 2)
print(f'Result after div of zero method truediv {(point_1 / point_4).get_all_point_this()}')

point_4.set_x(10)
print(f'Result div after changes x method truediv {(point_1 / point_4).get_all_point_this()}')
