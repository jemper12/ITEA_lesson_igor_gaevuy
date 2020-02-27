"""
Создать список из N элементов (от 0 до n с шагом 1). В этом списке вывести все четные значения.
"""

n = input('input number')
list_number = list(range(int(n)))
for num in list_number:
    if not num % 2 and num != 0:
        print(num)
