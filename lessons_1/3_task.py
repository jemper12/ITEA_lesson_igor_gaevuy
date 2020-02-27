"""
Напишите программу, которая выводит на экран числа от 1 до 100.
При этом вместо чисел, кратных трем, программа должна выводить слово Fizz,
а вместо чисел, кратных пяти — слово Buzz.
Если число кратно пятнадцати, то программа должна выводить слово FizzBuzz.
"""


def test_num(num):
    if not num % 15:
        print('FizzBuzz')
    elif not num % 5:
        print('Buzz')
    elif not num % 3:
        print('Fizz')
    else:
        print(num)


for number in range(101):
    if number == 0:
        continue
    test_num(number)
