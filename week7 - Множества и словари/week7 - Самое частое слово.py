# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:27:58 2017

@author: Maria
"""

# Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше
# в лексикографическом порядке.
# Формат ввода
# Вводится текст.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# apple orange banana banana orange
#
# Вывод программы:
# banana
#
# Тест 2
# Входные данные:
# oh you touch my tralala mmm my ding ding dong
#
# Вывод программы:
# ding
#
# Тест 3
# Входные данные:
# q w e r t y u i o p
# a s d f g h j k l
# z x c v b n m
#
# Вывод программы:
# a

fin = open('input.txt', 'r', encoding='utf8')
fout = open('output.txt', 'w', encoding='utf8')

lines = list()
for line in fin:
    lines.append(line.split())

Words = dict()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        x = lines[i][j]
        if x not in Words:
            Words[x] = 0
        else:
            Words[x] += 1

Max = 0
for key, value in Words.items():
    if Max < value:
        Max = value

for i in sorted(Words.items(), key=lambda x: x[0]):
    if i[1] == Max:
        print(i[0], file=fout)
        break

fin.close()
fout.close()
