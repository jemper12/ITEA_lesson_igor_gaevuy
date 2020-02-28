"""
Создать класс автомобиля. Описать общие аттрибуты. Создать классы легкового автомобиля и грузового.
Описать в основном классе базовые аттрибуты для автомобилей.
Будет плюсом если в классах наследниках переопределите методы базового класса.
"""
from random import randrange as rand


class Car:
    engine = 'Gasoline'
    drive = "front"

    def __init__(self, color, transmission):
        self._color = color
        self._transmission = transmission


class PassengerCar(Car):
    weight = rand(0, 4)
    speed = rand(70, 240)
    type_car = 'passenger'

    def __init__(self, color, transmission, driver):
        super().__init__(color, transmission)
        self._driver = driver

    def get_driver(self):
        return self._driver

    def set_driver(self, to):
        if type(to) is str:
            self._driver = to
        else:
            print('error, not correct type variable')

    def get_detaly(self):
        data = f'car type = {self.type_car}\ncolor car = {self._color}\ndriver = {self._driver}\n'
        return data


class Cargo(Car):
    weight = rand(5, 10)
    speed = rand(30, 90)
    type_car = 'cargo'

    def __init__(self, color, transmission, driver):
        super().__init__(color, transmission)
        self._driver = driver

    def get_driver(self):
        return self._driver

    def set_driver(self, to):
        if type(to) is str:
            self._driver = to
        else:
            print('error, not correct type variable')

    def get_detaly(self):
        data = f'car type = {self.type_car}\ncolor car = {self._color}\ndriver = {self._driver}\n'
        return data


car1 = PassengerCar('red', 'auto', 'Ivan')
car1.set_driver('Andrey')

car2 = Cargo('white', 'mechanical', 'Igor')

print(car1.get_detaly())
print(car2.get_detaly())
