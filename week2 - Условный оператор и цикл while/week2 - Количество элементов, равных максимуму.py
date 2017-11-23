# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:22:23 2017

author: Maria Zorkaltseva
"""

# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите, какое количество элементов этой последовательности, равны ее 
# наибольшему элементу.

n = int(input())
i = 0
Max = 0
while n != 0:
    if Max < n:
        Max = n
        i = 1
    elif n == Max:
        i = i + 1
    n = int(input())
print(i)
