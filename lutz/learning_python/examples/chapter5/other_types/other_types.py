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
print(float(x), float(z))
print(float(x + z), float(17 / 6))
print(Fraction.from_float(1.75))
print(Fraction(*1.75.as_integer_ratio()))

print(Fraction(1, 3) + 2)  # результат объект дроби.
print(Fraction(1, 3) + 2.0)  # результат объект с плавающей точкой.
print(Fraction(1, 3) + (1.0 / 3))  # результат объект с плавающей точкой.

print(4.0 / 3)
print((4.0 / 3).as_integer_ratio())
a = Fraction(1, 3) + Fraction(*(4.0 / 3).as_integer_ratio())
print(a, a.limit_denominator())
