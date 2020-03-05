"""
Создать класс комплексного числа и реализовать для него арифметические операции.
"""


class ComplexNumber:
    def __init__(self, real, imaginary):
        self._real = real
        self._imaginary = imaginary

    """Сложение"""

    def __add__(self, other):
        return ComplexNumber((self._real + other.get_real_part()), (self._imaginary + other.get_imaginary_part()))

    """Отнимание"""

    def __sub__(self, other):
        return ComplexNumber((self._real - other.get_real_part()), (self._imaginary - other.get_imaginary_part()))

    """Умножение"""

    def __mul__(self, other):
        return ComplexNumber((self._real * other.get_real_part() - self._imaginary * other.get_imaginary_part()),
                             (self._imaginary * other.get_real_part() + self._real * other.get_imaginary_part()))

    """Деление"""

    def __truediv__(self, other):
        return ComplexNumber((self._real * other.get_real_part() + self._imaginary * other.get_imaginary_part()) / (
                    other.get_real_part() ** 2 + other.get_imaginary_part() ** 2),
                             ((self._imaginary * other.get_real_part() - self._real * other.get_imaginary_part()) / (
                                         other.get_real_part() ** 2 + other.get_imaginary_part() ** 2)))

    def get_complex_number(self):
        if self._imaginary > 0:
            return f'z = {self._real} + {self._imaginary}i'
        elif self._imaginary < 0:
            return f'z = {self._real} - {-self._imaginary}i'

    def get_real_part(self):
        return self._real

    def get_imaginary_part(self):
        return self._imaginary


first_number = ComplexNumber(3, -6)
print(f'first complex number {first_number.get_complex_number()}')
second_number = ComplexNumber(7, 2)
print(f'second complex number {second_number.get_complex_number()}')

print(f'result sum complex numbers ({(first_number + second_number).get_complex_number()})')
print(f'result sub complex numbers ({(first_number - second_number).get_complex_number()})')
print(f'result mul complex numbers ({(first_number * second_number).get_complex_number()})')
print(f'result div complex numbers ({(first_number / second_number).get_complex_number()})')
