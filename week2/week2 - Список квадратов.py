# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:14:04 2017

author: Maria Zorkaltseva
"""

# -----task10-----
# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.

n = int(input())
i = 1
while i**2 <= n:
    temp = i**2
    print(temp, end=' ')
    i = i + 1
