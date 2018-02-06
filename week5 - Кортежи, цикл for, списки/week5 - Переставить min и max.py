# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:54:16 2018

author: Maria Zorkaltseva
"""

# В списке все элементы различны. Поменяйте местами минимальный и
# максимальный элемент этого списка.
# Формат ввода
# Вводится список целых чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# 3 4 5 2 1
# Вывод программы:
# 3 4 1 2 5 
#
# Тест 2
# Входные данные:
# 1 5 4 3 2
# Вывод программы:
# 5 1 4 3 2 
#
# Тест 3
# Входные данные:
# -30000 30000
# Вывод программы:
# 30000 -30000

numList = list(map(int, input().split()))
temp = 0
if (len(numList) != 0):
    Min = numList[0]
    Max = numList[0]

for i in range(0, len(numList)):
    if (Min >= numList[i]):
        Min = numList[i]
        IndexMin = i
    if (Max <= numList[i]):
        Max = numList[i]
        IndexMax = i
temp = numList[IndexMin]
numList[IndexMin] = numList[IndexMax]
numList[IndexMax] = temp
print(' '.join(map(str, numList)))