x = set('abcde')
y = set('bdxyz')
print(x, y)
print(x - y)
print(x | y)
print(x & y)
print(x ^ y)
print(x > y, x < y, x == y)
print('e' in x)

z = x.intersection(y)
print(z)
z.add('spam')
print(z)
z.update(['x', 'y'])
print(z)
z.remove('b')
print(z)

for item in set('abc'):
    print(item * 3)

S = {1, 2, 3}
print(S | {3, 4})
# print(S | [3, 4]) вызовет ошибку, но методы разрешают взаимодействие с любыми типами...
print(S.union([3, 4]))
print(S.intersection((1, 3, 5)))
print(S.issubset(range(-5, 5)))
print(S.issubset(range(3, 5)))

S1 = {1, 2, 3, 4}
print(S1, S1 & {1, 3}, {1, 5, 3, 6} | S1, S1 - {1, 3, 4}, S1 > {1, 3}, S1 > {1, 3, 4, 5})
print(S1 - {1, 2, 3, 4})
print(type({}))  # !!!
S = set()  # Инициализация пустого множества.

S2 = {0}
# S2.add([1, 2, 3]) вызовет ошибку из-за того, что список нехешируемый тип.
# S2.add({'a': 1, 'b': 2, 'c': 3}) вызовет ошибку из-за того, что список нехешируемый тип, но...
S2.add((1, 2, 3))  # Работает со словарями/
print(S2)

print({x ** 2 for x in [1, 3, 3, 4]})  # Интересно!!!
print({letter * 2 for letter in 'spaaam'})

L = ['a', 'b', 'a', 'c', 'b', 'd', 'e']
print(L)
L = list(set(L))
L.sort()
print(L)
