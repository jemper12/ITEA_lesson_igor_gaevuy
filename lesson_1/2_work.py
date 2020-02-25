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
