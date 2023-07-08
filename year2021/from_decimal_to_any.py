"""
Переводит любое число из десятичной системы счисления в любую другую.
Основание системы счисления можно задать.
"""

number = int(input('Enter a number: '))
base = int(input('Enter a base of numeral system: '))

while number > 0:
    print(number % base, end='')
    number //= base
