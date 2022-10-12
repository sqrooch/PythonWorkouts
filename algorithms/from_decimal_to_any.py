number = int(input('Enter a number: '))
base = int(input('Enter a base of numeral system: '))

while number > 0:
    print(number % base, end='')
    number //= base

