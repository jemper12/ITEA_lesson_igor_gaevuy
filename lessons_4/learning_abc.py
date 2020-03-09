from abc import abstractmethod, ABC


class AbstractVehicle(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def beep(self):
        print('BEEP')


class Vehicle(AbstractVehicle):

    def __init__(self, model, engine):
        self._model = model
        self._engine = engine

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, to):
        self._model = to

    def drive(self):
        print('asdasda')
        # super().drive()

    def beep(self):
        super().beep()


auto = Vehicle('BMW', 'v8')
auto.drive()
print(auto.model)
auto.model = 'Lanos'
print(auto.model)
