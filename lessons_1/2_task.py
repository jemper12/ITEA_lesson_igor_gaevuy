'''
Создать словарь Страна:Столица. Создать список стран.
Не все страны со списка должны сходиться с названиями стран со словаря.
С помощою оператора in проверить на вхождение элемента страны в словарь,
и если такой ключ действительно существует вывести столицу.
'''

dict_country = {
    'United Arab Emirates': 'Abu Dhabi',
    'Nigeria': 'Abuja',
    'Ghana': 'Accra',
    'Pitcairn Islands': 'Adamstown',
    'Ethiopia': 'Addis Ababa'
}
list_country = ['Nigeria', 'United Arab Emirates', 'Algeria', 'Andorra']
for country, city in dict_country.items():
    if country in list_country:
        print(city)
