# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:06:30 2017

author: Maria Zorkaltseva
"""

#Даны три целых числа. Найдите наибольшее из них 
#(программа должна вывести ровно одно целое число).
#Какое наименьшее число операторов сравнения (>, <, >=, <=)
# необходимо для решения этой задачи?

A = int(input())
B = int(input())
C = int(input())
max = 0
if A >= B and A >= C:
    max = A
elif B >= A and B >= C:
    max = B
elif C >= A and C >= B:
    max = C
print(max)
