def bank(summ, year, percent):
    a = summ + summ * percent * (365 * year) / 365 / 100
    print(a)


bank(int(input('summa\n')), int(input('year\n')), int(input('percent\n')))
