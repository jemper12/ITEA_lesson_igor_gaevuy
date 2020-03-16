"""
Создать подобие социальной сети. Описать классы, которые должны выполнять соответствующие функции
    (Предлагаю насследовать класс авторизации от класса регистрации).
Добавить проверку на валидность пароля (содержание символов и цифр), проверка на уникальность логина пользователя.

Человек заходит, и имеет возможность зарегистрироваться (ввод логин, пароль, потдверждение пароля),
    далее входит в свою учетную запись.

Добавить возможность выхода из учетной записи, и вход в новый аккаунт.

Создать класс User, котоырй должен разделять роли обычного пользователя и администратора.

При входе под обычным пользователем мы можем добавить новый пост, с определённым содержимим,
    так же пост должен содержать дату публикации.

Под учётной записью администратора мы можем увидеть всех пользователей нашей системы, дату их регистрации, и их посты.'''
"""
import shelve
import re
from datetime import datetime

# datetime.today().strftime("%Y-%m-%d")

USER_DB = 'users'
POST_DB = 'posts'


class Registration:

    def __init__(self, username, password, is_super=False):
        self._username = username
        self._password = password
        self._is_super = is_super

    def valid_password(self):
        if len(self._password) < 6:
            print(f'Password must be 6 characters or more')
            return None

        if re.match(r'\s', self._password):
            print(f'Space in password')
            return None

        if re.search(r'[0-9]', self._password) is None:
            print(f'Not number in password')
            return None

        if re.search(r'[a-z]', self._password) is None:
            print('Need small letters in the password')
            return None

        if re.search(r'[A-Z]', self._password) is None:
            print('Need big letters in the password')
            return None

        return True

    def valid_username(self):
        if re.match(r'\s', self._username):
            print(f'Space in username')
            return None
        return True

    def registration_user(self):
        """
        True if user valid and created
        False if user already created
        None is user not valid
        """
        if self.valid_password() is True and self.valid_username() is True:
            with shelve.open(USER_DB) as db:
                if db.get(self._username) is None:
                    db[self._username] = {'password': self._password,
                                          'is_admin': self._is_super,
                                          'date': datetime.today().strftime("%Y-%m-%d")
                                          }
                    print('User created successfully')
                    with shelve.open(POST_DB) as post:
                        post[self._username] = []
                    return True
                else:
                    print(f'User is already registered')
                    return False
        return None


class Authorization(Registration):

    def user_verification(self):
        with shelve.open(USER_DB) as db:
            user = db.get(self._username)
            if user and user['password'] == self._password:
                print('Hello my friend')
                return user
            else:
                print('Oh no, you forgot your password')
                return False


class Users:
    _login_in_sys = False

    def __init__(self, username, password):
        start_ = Authorization(username, password).user_verification()
        if start_ is not False:
            self._username = username
            self._is_admin = start_['is_admin']
            self._date_registration = start_['date']
            self.status_login = True

    def add_post(self, title, text):
        if title is "":
            print('Title is empty')
            return None
        if text is "":
            print('Body post is empty')

        with shelve.open(POST_DB) as db:
            db[self._username] = db[self._username] + [{'date': datetime.today().strftime("%Y-%m-%d"),
                                                        'title': title,
                                                        'text': text}]
        return True

    def get_all_post(self):
        with shelve.open(POST_DB) as db:
            if self._is_admin is True:
                for user, data in db.items():
                    print(f'Author = {user}, registration = {self._date_registration}')
                    for post in data:
                        print(f'\t# {post["date"]} - {post["title"]} - {post["text"]}')
            else:
                print(f'Author = {self._username}, registration = {self._date_registration}')
                for post in db.get(self._username):
                    print(f'\t# {post["date"]} - {post["title"]} - {post["text"]}')

    def get_all_users(self):
        if self._is_admin is True:
            with shelve.open(USER_DB) as db:
                for username, data in db.items():
                    print(username, data[username]['date'])
        else:
            print('Only to ADMIN\n')

    def logout(self):
        self.status_login = False

    @property
    def status_login(self):
        return self._login_in_sys

    @status_login.setter
    def status_login(self, to):
        self._login_in_sys = to


# print(Registration('igor', 'AasdasrA1').valid_username())

def registration():
    while True:
        print('For registration need entered several fields\n')
        username = input('Please enter your username, it should not only contain spaces, '
                         'remember it, it is not difficult at all\n')
        password1 = input('Now think of the most secure password in the world\n')
        password2 = input('Try again password\n')

        if password1 != password2:
            print('Your password is so strong that you yourself could not repeat it')
            continue
        admin_test = input('Would you like to be an admin?\n уes or no\n')

        if admin_test == 'yes':
            user = Registration(username, password1, True).registration_user()
        else:
            user = Registration(username, password1).registration_user()

        if user is not True:
            continue_to_register = input('Something went wrong, but you already know it yourself. '
                                         'If you want to try disappearing once enter anything, if not enter 0\n')
            if continue_to_register == '0':
                break

        else:
            print('Super, now you can log in\n')
            break


def login():
    print('Ok, for this you need to enter 2 main words\n')
    username = input('Enter you username\n')
    password = input('Enter you password\n')
    user = Users(username, password)
    if user.status_login is False:
        print('You enter not valid username or password\n')
        return

    while True:
        working = input('Enter a number to interact\n'
                        '1) Create post\n'
                        '2) Get post\n'
                        '3) Logout\n'
                        '4) Get all Users (ONLY ADMIN)\n')
        if working == '1':
            title = input('Ok, Now please enter title for you post\n')
            post = input('And now you can write your post\n')
            user.add_post(title, post)
        elif working == '2':
            print('Ok, Behold this greatness of information\n')
            user.get_all_post()
        elif working == '3':
            break
        elif working == '4':
            user.get_all_users()
        else:
            print('Please enter corect number')


engine_progress = True
print('Hello, I small social network @SHARMANAMA@, our acquaintance will be interesting))))')
while True:
    start = input('If you sing in SHARMANAMA enter 1\nif you need registration enter 2\n')
    if start == '1':
        login()

    elif start == '2':
        registration()

    elif start == '3':
        break

    else:
        print('Please make your right choice. You need to completely choose between 1 and 2. '
              'But if you decide to leave, enter 3\n')
