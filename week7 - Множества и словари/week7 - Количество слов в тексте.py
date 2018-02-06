# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 23:46:10 2017

@author: Maria
"""

# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку
# sys) записан текст. Словом считается последовательность непробельных символов
# идущих подряд, слова разделены одним или большим числом пробелов или
# символами конца строки. Определите, сколько различных слов содержится
# в этом тексте.
# Формат ввода
# Вводится текст.
# Формат вывода
# Выведите ответ на задачу.

# Тест 1
# Входные данные:
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.
#
# Вывод программы:
# 19

fin = open('input.txt', 'r', encoding='utf8')

lines = []
Set = set()
for line in fin:
    lines.append(line.split())

for i in range(len(lines)):
    for j in range(len(lines[i])):
        Set.add(lines[i][j])

print(len(Set))
fin.close()
