# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def list_arithmetic_progression(list, size, d, x):
#     for i in range(2, size + 1):
#         list.append(x + (i - 1) * d)
#     return list
# size = int(input("Введите размер вашего массива: "))
# x = int(input("Введите первый элемент вашего массива: "))
# d = int(input("Введите разность в арифметической прогрессии: "))
# list = [x]
# print(list_arithmetic_progression(list, size, d, x))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# import random
# def selection(list, min, max, size):
#     list_selection = []
#     for i in range(size):
#         if min < list[i] < max:
#             list_selection.append(i)
#     return list_selection

# size = int(input("Введите размер массива: "))
# a = -10
# b = 10
# list = [random.randint(a, b) for i in range(size)]
# print(list)
# min = int(input("Введите нижний предел отбора: "))
# max = int(input("Введите верхний предел отбора: "))
# print(f"Индексы элементов входящих в заданный диапазон {selection(list, min, max, size)}")