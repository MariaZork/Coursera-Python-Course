# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 02:28:36 2017

@author: Maria
"""

# В олимпиаде участвовало N человек. Каждый получил определенное количество
# баллов, при этом оказалось, что у всех участников разное число баллов.
# Упорядочите список участников олимпиады в порядке убывания набранных баллов.
# Формат ввода
# Программа получает на вход число участников олимпиады N. Далее идет N строк,
# в каждой строке записана фамилия участника, затем, через пробел, набранное
# им количество баллов.
# Формат вывода
# Выведите список участников (только фамилии) в порядке убывания
# набранных баллов.

# Тест 1
# Входные данные:
# 3
# Ivanov 15
# Petrov 10
# Sidorov 20
#
# Вывод программы:
# Sidorov
# Ivanov
# Petrov
#
# Тест 2
# Входные данные:
# 3
# Ivanov 15
# Petrov 20
# Sidorov 10
#
# Вывод программы:
# Petrov
# Ivanov
# Sidorov
#
# Тест 3
# Входные данные:
# 3
# Ivanov 10
# Petrov 15
# Sidorov 20
#
# Вывод программы:
# Sidorov
# Petrov
# Ivanov

N = int(input())
MyList = []

for i in range(N):
    Tmp = input().split()
    Surname = Tmp[0]
    Score = int(Tmp[1])
    T = (Surname, Score)
    MyList.append(T)

MyList.sort(key=lambda Index: Index[1], reverse=True)
for i in range(0, len(MyList)):
    print(MyList[i][0], end=' ')
