"""
Задание:
Вернуть сумму всех чисел, меньше переданного числа и кратных 3 или 5. Если число отрицательное, вернуть 0.
Примечание: Если число кратно и 3, и 5, добавлять его в сумму только один раз.
"""


def solution(number):
    sum_result = 0  # В Python есть функция sum, которая суммирует итерируемые последовательности.
    if number < 0:  # Не нужный блок
        return 0
    for n in range(number):  # Можно заменить генераторным выражением.
        if n % 3 == 0:
            sum_result += n
        elif n % 5 == 0:  # Вместо elif короче использовать or
            sum_result += n
    return sum_result


print(solution(16))
print(solution(0))
print(solution(-3))

"""
Best practice:
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
    
Обратить внимание как работает генератор range с отрицательными числами!!!
"""
