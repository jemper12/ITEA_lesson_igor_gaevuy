"""
Реализовать функцию bank, которая приннимает следующие аргументы: сумма депозита, кол-во лет,
и процент. Результатом выполнения должна быть сумма по истечению депозита
"""


def bank(summ=68000, year=2, percent=13):
    a = summ + summ * percent * (365 * year) / 365 / 100
    return a


print(bank())
