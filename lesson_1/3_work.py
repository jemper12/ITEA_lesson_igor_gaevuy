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
