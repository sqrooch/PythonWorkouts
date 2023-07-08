def insert_sort(arr):
    """
    Пробегает по массиву чисел. Сравнивает рядом лежащие числа. Меняет их местами, если один больше другого.
    :param arr: массив чисел.
    :return: отсортированный массив.
    """
    for i in range(1, len(arr)):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr


def choice_sort(arr):
    """
    Проходит двумя циклами по массиву и меняет местами элементы из циклов, если один меньше другого.
    :param arr: массив чисел.
    :return: отсортированный массив.
    """
    length_array = len(arr)
    for i in range(length_array - 1):
        for j in range(i + 1, length_array):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def bubble_sort(arr):
    """
    Пузырьковый алгоритм. Участвуют два цикла.
    Каждая итерация первого цикла продвигает наибольшее число в массиве вправо
    с помощью поэлементного сравнения во втором цикле.
    :param arr: массив чисел.
    :return: отсортированный массив.
    """
    length_array = len(arr)
    for i in range(1, length_array):
        for j in range(length_array - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


array = [5, -2, 9, -2.15, 5.2, -99]
print(insert_sort(array))
array = [5, -2, 9, -2.15, 5.2, -99]
print(choice_sort(array))
array = [5, -2, 9, -2.15, 5.2, -99]
print(bubble_sort(array))
