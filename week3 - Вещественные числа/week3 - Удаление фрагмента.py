# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 23:59:27 2017

author: Maria Zorkaltseva
"""

# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h, а также
# все символы, находящиеся между ними.
# Формат ввода
# Вводится строка.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# In the hole in the ground there lived a hobbit
# Вывод программы:
# In tobbit
#
# Тест 2
# Входные данные:
# qwertyhasdfghzxcvb
# Вывод программы:
# qwertyzxcvb

S = input()
pos1 = S.find('h')
pos2 = S.rfind('h')
i = 0
while i < len(S):
    if pos1 <= i and i <= pos2:
        S.replace(S[i], '')
    else:
        print(S[i], end='')
    i = i + 1