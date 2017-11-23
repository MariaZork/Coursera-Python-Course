# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:17:18 2017

author: Maria Zorkaltseva
"""

# Последовательность состоит из натуральных чисел, не превосходящих 10⁹,
# и завершается числом 0.Определите значение наибольшего элемента 
# последовательности.

x = int(input())
max_elem = 0
while x != 0:
    if x > max_elem:
        max_elem = x
    x = int(input())
print(max_elem)
