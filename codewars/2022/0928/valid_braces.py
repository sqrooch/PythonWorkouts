"""
Напишите функцию, которая принимает строку фигурных скобок и определяет, допустим ли порядок этой комбинации скобок.
Функция должна возвращать true, если строка допустима, и false, если она недопустима.

Входящая тестовая строка обязана быть непустой и состоять только из трёх видов фигурных скобок: ()[]{}.
Строка фигурных скобок считается допустимой, если все скобки в строке соответствуют логичной конструкции.

Например:
Строка "(){}[]"   даст  True
Строка "([{}])"   даст  True
Строка "(}"       даст  False
Строка "[(])"     даст  False
Строка "[({})](]" даст  False
"""


def valid_braces(string):
    braces = ('(', ')'), ('[', ']'), ('{', '}')
    char_list = list(string)

    while char_list:
        got_box = False  # Обнаружение парных скобок: (), [] или {}. В начале цикла по умолчанию всегда False.
        for i in range(len(char_list))[:-1]:
            if (char_list[i], char_list[i + 1]) in braces:
                got_box = True  # Парные скобки обнаружены.
                char_list.pop(i)  # Удаляем парные скобки из списка.
                char_list.pop(i)
                break

        if not got_box:  # Парные скобки не обнаружены. Строка считается бракованной.
            return False

    return True  # Список пуст. Найдены все парные скобки, значит строка считается допустимой.


""" Более изящное решение:

def valid_braces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0
"""

print(valid_braces('(){}[]'))
print(valid_braces('([{}])'))
print(valid_braces('(}'))
print(valid_braces('[(])'))
print(valid_braces('[({})](]'))
