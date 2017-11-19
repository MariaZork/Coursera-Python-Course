# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:23:20 2017

author: Maria Zorkaltseva
"""

# Дана последовательность натуральных чисел, завершающаяся числом 0. 
# Определите,какое наибольшее число подряд идущих элементов этой 
# последовательности равны друг другу.

n0 = int(input())
n = -1
eq = 1
maxeq = 0
while n != 0:
    n = int(input())
    Next = n
    if n0 == n:
        eq = eq + 1
    else:
        eq = 1
    if maxeq < eq:
        maxeq = eq
    n0 = n
print(maxeq)
