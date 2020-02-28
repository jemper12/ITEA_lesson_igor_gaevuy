"""
Создать класс магазина.
Конструктор должен инициализировать значения: «Название магазина» и «Количество проданных товаров».
Реализовать методы объекта, которые будут увеличивать кол-во проданных товаров,
и реализовать вывод значения переменной класса,
которая будет хранить общее количество товаров проданных всеми магазинами.
"""


class Shop:
    quantity_all = 0

    def __init__(self, shop_name, quantity_of_goods_sold):
        self._shop_name = shop_name
        self._quantity_of_goods_sold = quantity_of_goods_sold
        Shop.quantity_all += quantity_of_goods_sold

    def add_quantity(self, count):
        self._quantity_of_goods_sold = self._quantity_of_goods_sold + count
        Shop.quantity_all += count

    def get_quantity(self):
        return self._quantity_of_goods_sold


shop1 = Shop('baracuda', 15)
'''Количество проданых товаров в первом магазине до дополнительных продаж'''
print(f'The number of items sold in the first store until additional sales = {shop1.get_quantity()}')

shop1.add_quantity(25)
'''Количество проданых товаров в первом магазине после дополнительных продаж'''
print(f'The number of items sold in the first store = {shop1.get_quantity()}')

shop2 = Shop('baracuda', 15)
'''Количество проданых товаров в втором магазине'''
print(f'The number of items sold in the second store = {shop2.get_quantity()}')

'''Количество проданых товаров всеми магазинами'''
print(f'The number of items sold in the all store = {Shop.quantity_all}')
