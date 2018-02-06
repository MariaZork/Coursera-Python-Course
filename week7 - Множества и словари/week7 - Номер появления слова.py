# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 02:47:08 2017

@author: Maria
"""

# Во входном файле (вы можете читать данные из файла input.txt) записан текст.
# Словом считается последовательность непробельных подряд идущих символов.
# Слова разделены одним или большим числом пробелов или символами конца строки.
# Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось
# в этом тексте ранее.
# Формат ввода
# Вводится текст.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# one two one tho three
#
# Вывод программы:
# 0 0 1 0 0 
#
# Тест 2
# Входные данные:
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
#
# Вывод программы:
# 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0

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
            Words[lines[i][j]] = 0
        else:
            Words[lines[i][j]] += 1
        print(Words[lines[i][j]], end=' ', file=fout)

fin.close()
fout.close()
