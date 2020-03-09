class Cat:
    def __init__(self, name, weight):
        self._name = name
        self._weight = weight

    def __add__(self, other):
        return Cat(self._name + other._name, self._weight + other._weight)
        # return len(self) + len(other)

    def __len__(self):
        return 1


cat = Cat('kitty', 3)
cat2 = Cat('cat', 5)

cat3 = cat + cat2 + cat2
print(cat3._name, cat3._weight)
#################################


from itertools import zip_longest

to_square = lambda x, y: (x ** 2, y ** 2)

list2 = [1, 2, 3, 4, 5]
list1 = [6, 3, 4, 6, 2, 2]

result = map(to_square, list1, list2)

print(tuple(result))

print(list(filter(lambda x: not x % 2, list1)))

a = [5, 6, 7, 4]
b = [3, 55, 7, 3, 1, 6]

print(list(zip_longest(a, b, fillvalue=True)))

####################### 2 ###########################
# class Phone:
#     mobile_type = 'Common phone'
#
#     def __init__(self, model, imei):  # Конструктор класса
#         self._model = model
#         self._imei = imei
#
#     def call(self, to):
#         self._connect_to_another_device(to)
#         print(f'Okey, i am calling {to} from {self._model}')
#
#     def _connect_to_another_device(self, to):
#         print(f'Some connection magic {to}')
#
#     def get_model(self):  ##### Гетер
#         return self._model
#
#     def set_model(self, value):  ##### Сетер
#         self._model = value
#
#     def get_imei(self):
#         return self._imei
#
#     def set_imai(self, value):
#         self._imei = value
#
#
# class MobilePhone(Phone):  # Наследование
#
#     def send_messege(self, messege_text, to):
#         print(f' sending messege {messege_text} to {to}')
#
#
# class SatelitePhone(Phone):
#
#     def call(self, satelite_coordinates, to):
#         print(f'Caliing {to} from {self.get_model()} satelite: {satelite_coordinates}')
#
#
# class Application:
#     def __init__(self, name, marketplace, ):
#         self._name = name
#         self._marketplace = marketplace
#         self._downloaded = False
#
#     def start(self):
#         if self._downloaded:
#             print(f'starting the {self._name} application')
#
#     def downloaded(self):
#         print(f'Downloaded {self._name} from {self._marketplace}')
#         self._downloaded = True
#
#
# # Agregation
# class SmartPhone1(MobilePhone):
#     """
#     Ассоциация - гласит, что фттрибутами обьекта могут быть обьекты другого класса
#     Композиция - обьект создается внутри класса, и дальше обрабатывается
#     Аггрегация - обьект создается ВНЕ класса, передается в обьекту класса
#     """
#
#     def play_audio(self):
#         print("Play adudio")
#
#     def play_video(self):
#         print('Play video')
#
#     # def downloaded_application(self, app_name, market_place):
#     #     app = Application(app_name, market_place)
#     #     app.downloaded()
#     #     self._app = app
#
#     # Waiting for object type Application
#     def start_application(self, application_obj):
#         application_obj.start()
#
#
# # Composition
# class SmartPhone2(MobilePhone):
#     """
#     Ассоциация - гласит, что фттрибутами обьекта могут быть обьекты другого класса
#     Композиция - обьект создается внутри класса, и дальше обрабатывается
#     Аггрегация - обьект создается ВНЕ класса, передается в обьекту класса
#     """
#
#     def play_audio(self):
#         print("Play adudio")
#
#     def play_video(self):
#         print('Play video')
#
#     def downloaded_application(self, app_name, market_place):
#         app = Application(app_name, market_place)
#         app.downloaded()
#         self._app = app
#
#     # Starting app obj and that already created
#     def start_application(self):
#         self._app.start()
#
#
# smartphone = SmartPhone1('Apple', '+34545324234')
# app = Application('Printing', 'PlayMarket')
# app.downloaded()
# smartphone.start_application(app)
#
# # mobile_phone = MobilePhone('model', '+35678902353463')
# # mobile_phone.call('389939485')
# # mobile_phone.send_messege('Hello man', '+923482934894839483943')
# # print(mobile_phone.get_model())
# #
# # satelite_phone = SatelitePhone('GrulLamash', '+34858398593485')
# # satelite_phone.call('60,54/23,65', '+345090903495')

# ##########################1##############################
#
# class Phone:
#     mobile_type = 'Common phone'
#
#     def __init__(self, model, imei):  # Конструктор класса
#         self.model = model
#         self.imei = imei
#
#     def call(self, to):
#         print(f'Okey, i am calling {to} from {self.model}')
# print(Phone.mobile_type)
#
# phone = Phone('Nokia', 'EZ12345678')
#
# phone.call("+380936081715")
# phone.imei = 'JLAJKSKDJLASKD'
#
# print(phone.imei)
#
# Phone.mobile_type = 'asdasdjasdk'
#
# # Создание дополнительных переменных класа
# phone.phone_number = '+23409034'
# print(phone.phone_number)
#
# # Изменение пременной класа
#
#
# phone2 = Phone('Siemens', 'EZ85849389453')
# phone2.call('+380677734344')
#
# print(phone2.imei)
# print(phone2.mobile_type)

########################1##########################
