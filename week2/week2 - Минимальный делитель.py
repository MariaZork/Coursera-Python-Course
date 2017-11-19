# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:15:27 2017

author: Maria Zorkaltseva
"""

# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, 
# отличный от 1.

n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)
