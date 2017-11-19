# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:05:38 2017

author: Maria Zorkaltseva
"""

# Даны два целых числа. Программа должна вывести число 1, 
# если первое число больше второго, число 2, если второе 
# больше первого или число 0, если они равны.

A = int(input())
B = int(input())
if A > B:
    print(1)
elif B > A:
    print(2)
else:
    print(0)