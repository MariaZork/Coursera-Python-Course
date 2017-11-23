# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 00:03:36 2017

author: Maria Zorkaltseva
"""

# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов.
# Формат ввода
# Вводится строка.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# Hello world
# Вывод программы:
# 2

S = input()
i = 0
count = 0
while i < len(S):
    if S[i] == ' ':
        count = count + 1
    i = i + 1
print(count + 1)