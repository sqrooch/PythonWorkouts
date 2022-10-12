s = """
«Единство, — возвестил оракул наших дней, —
Быть может спаяно железом лишь и кровью...»
Но мы попробуем спаять его любовью, —
А там увидим, что прочней...
"""

sum_codes = 0
for ch in s:
    print(ord(ch))
    sum_codes += ord(ch)
print(sum_codes)
print([ord(ch) for ch in s])
print(list(map(ord, s)))
