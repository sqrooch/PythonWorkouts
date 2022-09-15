import math
import random

a = 3
b = 4
print(b * 3, b / 2)
print(b / (2.0 + a))
print(1 / 2.0)

num = 1 / 3.0
print(num)
print('%e' % num)
print('%4.2f' % num)  # это строка
print('{0:4.2f}'.format(num))  # это строка

print(repr('spam'))
print(str('spam'))

print(str(b'xy', 'utf8'))

X = 2
Y = 4
Z = 6
print(X < Y < Z, (X < Y) and (Y < Z))
print(X < Y > Z, (X < Y) and (Y > Z))
print(1 < 2 < 3.0 < 4)  # произвольное количество элементов в выражении.

print(1 == 2 < 3)  # даст False, потому что это то же, что (1 == 2 and 2 < 3), но не то же, что (False < 3).
print(1.1 + 2.2 == 3.3)  # даст False, потому что...
print(1.1 + 2.2)  # =3.3000000000000003 (ограниченная точность), но...
print(int(1.1 + 2.2) == int(3.3))  # даст True.

print(10 / 4, 10 // 4, Y // Z, Y / float(Z))

print(math.floor(2.5), math.floor(-2.5), math.trunc(2.5), math.trunc(-2.5))

print(1j * 1j, 2 + 1j * 3, (2 + 1j) * 3)

print(0o1, 0o20, 0o377)
print(0x1, 0x10, 0xFF)
print(0b1, 0b10000, 0b11111111)

print(0xFF, (15 * (16 ** 1) + 15 * (16 ** 0)))
print(0x2F, (2 * (16 ** 1) + 15 * (16 ** 0)))
print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))

print(oct(64), hex(64), bin(64))
print(64, 0o100, 0x40, 0b1000000)
print(int('64', 10), int('0o100', 8), int('0x40', 16), int('0b1000000', 2))
print(int('64', 10), int('0o100', 8), int('0x40', 16), int('0b1000000', 2))

print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x' % (64, 64))  # не поддерживает формат %b.

x = 1
y = 2
z = 4
print(bin(x), bin(y))  # x = 0001   y = 0010
print(x << y, bin(x << y))
print(z >> y, bin(z >> y))
print(x | y, bin(x | y))
print(x & y, bin(x & y))
print(y & y, bin(y & y))
print(x ^ y, bin(x ^ y))
print(y ^ y, bin(y ^ y))

X = 99
print(bin(X), X.bit_length(), len(bin(X)) - 2)

print(math.pi, math.e)
print(math.pi, math.e)
print(math.pi, math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144))
print(pow(2, 4), pow(4, 2.6))
print(abs(-46.6))
print(sum((1, 2, 3)), sum([1, 2, 3]))
print(min(-9, 1, 2, 4), max(-9, 1, 2, 4))

print(math.floor(2.567), math.floor(-2.567))
print(math.trunc(2.567), math.trunc(-2.567))
print(int(2.567), int(-2.567))
print(round(2.567), round(2.467), round(2.567, 2))  # производит число с плавающей точкой в памяти.
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))  # выдаёт строку, а не число.

print(random.random())
print(random.randint(0, 3))
letters = ['a', 'b', 'c', 'd']
print(letters)
print(random.choice(letters))
random.shuffle(letters)
print(letters)
