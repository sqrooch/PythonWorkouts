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
