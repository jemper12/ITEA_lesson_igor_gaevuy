dict_country = {
    'United Arab Emirates': 'Abu Dhabi',
    'Nigeria': 'Abuja',
    'Ghana': 'Accra',
    'Pitcairn Islands': 'Adamstown',
    'Ethiopia': 'Addis Ababa'
}
list_country = ['Nigeria', 'United Arab Emirates', 'Algeria', 'Andorra']
for country in dict(dict_country):
    if country in list_country:
        print(dict_country[country])
