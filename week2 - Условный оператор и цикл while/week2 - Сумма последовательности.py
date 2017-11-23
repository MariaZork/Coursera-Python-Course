# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:19:30 2017

author: Maria Zorkaltseva
"""

# Определите сумму всех элементов последовательности, завершающейся числом 0.

n = int(input())
Sum = 0
while n != 0:
    Sum = Sum + n
    n = int(input())
print(Sum)
