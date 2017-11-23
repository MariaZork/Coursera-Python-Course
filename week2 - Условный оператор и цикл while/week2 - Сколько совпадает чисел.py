# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:10:07 2017

author: Maria Zorkaltseva
"""

# Даны три целых числа. Определите, сколько среди них совпадающих. Программа 
# должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает)
# или 0 (если все числа различны).

A = int(input())
B = int(input())
C = int(input())
if (A == B) and (A == C) and (B == C):
    print(3)
elif (A != B) and (A != C) and (B != C):
    print(0)
else:
    print(2)
