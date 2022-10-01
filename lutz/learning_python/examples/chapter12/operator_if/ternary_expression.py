X = 1
Y = ''
Z = 'printZ'
A = ((X and Y) or Z)  # Ответ будет неверным, потому что Y - False.
print(A)

Y = 'printY'
A = ((X and Y) or Z)  # Требует, чтобы часть Y была истинной.
print(A)

A = Y if X else Z  # Альтернативная тернарная форма. Если операнды относительно просты, то пользоваться нужно ей.
print(A)
A = [Z, Y][bool(X)]  # Вариант со смещением. Всегда проверяет и Z и Y. Не использует "ленивый выбор".
print(A)
print()


def f1():
    print('f1')
    return 0


def f2():
    print('f2')
    return 1


print(f1() or f2())
print(f1() and f2())  # Не выполняет f2(), потому что f1() - False.
print()

L = [1, 0, 2, 0, 'spam', '', 'ham', []]
print(list(filter(bool, L)))  # Получение истинных значений через фильтр.
print([x for x in L if x])  # Включения.
print(any(L), all(L))  # Накопление значений истинности.
