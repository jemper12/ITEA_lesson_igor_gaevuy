def bank(summ=68000, year=2, percent=13):
    a = summ + summ * percent * (365 * year) / 365 / 100
    return a


print(bank())
