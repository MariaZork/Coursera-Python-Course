# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 00:06:32 2017

author: Maria Zorkaltseva
"""

# Дана строка. Удалите из этой строки все символы @.
# Формат ввода
# Вводится строка.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# Bilbo.Baggins@bagend.hobbiton.shire.me
# Вывод программы:
# Bilbo.Bagginsbagend.hobbiton.shire.me

S = input()
i = 0
while i < len(S):
    if S[i] != '@':
        print(S[i], end='')
    else:
        print('', end='')
    i = i + 1