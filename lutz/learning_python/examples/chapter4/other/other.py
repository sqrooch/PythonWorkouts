import decimal
from fractions import Fraction

X = set('spam')
Y = {'h', 'a', 'm'}
print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)
print({n ** 2 for n in [1, 2, 3, 4]})
print(list({1, 2, 1, 2, 3}))
print(set('spam') - set('ham'))
print(set('spam') == set('samp'))
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'ham', 'spam'])

print(1 / 3)
print(2 / 3 + 1 / 2)
d = decimal.Decimal('3.141')
print(d + 1)

decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

f = Fraction(2, 3)
print(f, f + 1, f + Fraction(1, 2))

print(1 > 2, 1 < 2)
print(bool('spam'))
Z = None
print(Z)
L = [None] * 5
print(L)

print(type(L))
print(type(type(L)))

if isinstance(L, list):
    print('yes')
