import decimal
from fractions import Fraction

print(0.1 + 0.1 + 0.1 - 0.3)
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.10') - decimal.Decimal('0.3'))

print(decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.10) - decimal.Decimal(0.3))
decimal.getcontext().prec = 2
print(decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.10) - decimal.Decimal(0.3))
print(decimal.Decimal(str(0.1)) + decimal.Decimal(str(0.1)) + decimal.Decimal(str(0.10)) - decimal.Decimal(str(0.3)))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x, y)
print(x + y, x - y, x * y)

print(Fraction('0.25'), Fraction('1.25'))
print(Fraction('0.25') + Fraction('1.25'))

print(0.1 + 0.1 + 0.1 - 0.3)
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))
print(decimal.Decimal('0.10') + decimal.Decimal('0.10') + decimal.Decimal('0.10') - decimal.Decimal('0.30'))

print(2.5.as_integer_ratio())
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)
print(x)
print(x + z)
