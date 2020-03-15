"""
pip3 install beautifulsoup4

Создать консольную программу-парсер, с выводом прогноза погоды.
Дать возможность пользователю получить прогноз погоды в его локации ( по умолчанию) и в выбраной локации,
    на определенную пользователем дату. Можно реализовать, как консольную программу, так и веб страницу.
Используемые инструменты: requests, beatifulsoup, остальное по желанию.
На выбор можно спарсить страницу, либо же использовать какой-либо API.
"""
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import re

date_now = datetime.today().strftime("%Y-%m-%d")

URL = 'http://pogoda.meta.ua/en/Kyivska/Obukhivskyi/Obukhiv/'


def get_weather(date):
    """
    :parameter date format %Y-%m-%d (2020-12-12)
    :return dict min and max temperature"""
    req = requests.get(url=f'{URL}{date}/')
    soup = BeautifulSoup(req.text, features="html.parser")
    try:
        result_req = soup.findChild('div', {'id': f't{date}'}).find_next('strong', {'style': 'font-size:18px'}).text
    except AttributeError:
        print(f'Date {date} is not available for viewing\n')
        return None
    result = {
        'min': str(result_req).split('..')[0],
        'max': str(result_req).split('..')[1]
    }

    return result


request_result = get_weather(date_now)
while_status = True
print(f"""
                        Hello, today {date_now}
                        min temperature = {request_result["min"]}
                        max temperature = {request_result["max"]}
                        """)
while while_status:
    test = input(f'If u have find temperature for another day, input 1, if not input 2 fo exit\n')
    if test == '2':
        while_status = False

    elif test == '1':
        while_user_enter_date = True
        while while_user_enter_date:
            user_input_date = input('Please, enter date in format "2012-12-12"\n')

            if re.match(r'^20[0-9][0-9]-[0-1][0-9]-[0-3][0-9]$', user_input_date):
                request_result = get_weather(user_input_date)
                if request_result is not None:
                    print(f"""
                        Ok, weather on {user_input_date}
                        min temperature = {request_result["min"]}
                        max temperature = {request_result["max"]}
                    """)
                    while_user_enter_date = False

            elif user_input_date == '2':
                while_user_enter_date = False
                while_status = False

            else:
                print(f'You enter "{user_input_date}", it`s invalid date, please try again, or enter 2 fo exit\n')

    else:
        print(f'You enter an invalid request, please try again\n')
