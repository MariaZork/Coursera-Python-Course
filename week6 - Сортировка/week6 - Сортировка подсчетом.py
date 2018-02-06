# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 01:44:36 2017

@author: Maria
"""

# Дан список из N (N≤2*10⁵) элементов, которые принимают целые значения
# от 0 до 100.
# Отсортируйте этот список в порядке неубывания элементов.
# Выведите полученный список.
# Решение оформите в виде функции CountSort(A), которая модифицирует
# передаваемый ей список. Использовать встроенные функции сортировки нельзя.

# Тест 1
# Входные данные:
# 7 3 4 2 5
# Вывод программы:
# 2 3 4 5 7
#
# Тест 2
# Входные данные:
# 1 2 3 4 5 6 7 8 9 10
# Вывод программы:
# 1 2 3 4 5 6 7 8 9 10
#
# Тест 3
# Входные данные:
# 9 8 7 6 5 4 3 2 1 0
# Вывод программы:
# 0 1 2 3 4 5 6 7 8 9

numList = list(map(int, input().split()))
def CountSort(numlist, Max):
    Counts = [0] * (Max+1)
    for i in range(0, len(numlist)):
        Counts[numlist[i]] = Counts[numlist[i]] + 1
    index = 0
    for i in range(0, Max+1):
        for j in range(0, Counts[i]):
            numlist[index] = i
            index += 1
    return numlist

numList = CountSort(numList, max(numList))
for i in range(len(numList)):
    print(numList[i], end=' ')