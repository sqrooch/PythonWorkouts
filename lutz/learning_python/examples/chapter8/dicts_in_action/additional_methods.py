someDict = {'spam': 1, 'ham': 2, 'eggs': 3}
print(someDict.get('spam'))  # Предоставляет значение по ключу...
print(someDict.get('toast'))  # ...или None,если ключа не существует...
print(someDict.get('toast', 'standard_value'))  # ...или заданное значение, если ключа не существует.

print(someDict)
someDict.update({'muffin': 4, 'eggs': 100})  # совмещает два словаря с заменой уже существующих ключей.
print(someDict)

# Можно производить поиск через синтаксис "включений", но это медленнее, чем прямой поиск через методы.
print([key for (key, value) in someDict.items() if value == 2])
print([value for (key, value) in someDict.items() if key == 'ham'])
