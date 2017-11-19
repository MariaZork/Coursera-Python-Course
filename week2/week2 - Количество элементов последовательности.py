# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:20:20 2017

author: Maria Zorkaltseva
"""

# Определите количество четных элементов в последовательности, 
# завершающейся числом 0.

n = int(input())
i = 0
while n != 0:
    if n % 2 == 0:
        i = i + 1
    n = int(input())
print(i)
