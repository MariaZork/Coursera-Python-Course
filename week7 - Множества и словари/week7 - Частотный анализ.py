# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 22:12:55 2017

@author: Maria
"""

# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую
# строку. Слова должны быть отсортированы по убыванию их количества появления
# в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
# Указание.
# После того, как вы создадите словарь всех слов, вам захочется
# отсортироватьего по частоте встречаемости слова. Желаемого можно добиться,
# если создать список, элементами которого будут кортежи из двух элементов:
# частота встречаемости словаи само слово. Например, [(2, 'hi'),
# (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать
# список кортежей, при этом кортежи сравниваются по первому элементу, а если
# они равны —то по второму. Это почти то, что требуется в задаче.
# Формат ввода
# Вводится текст.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
#
# Вывод программы:
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your

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
            Words[x] = 1
        else:
            Words[x] += 1

for i in sorted(Words.items(), key=lambda x: (-x[1], x[0])):
    print(i[0], file=fout)

fin.close()
fout.close()
