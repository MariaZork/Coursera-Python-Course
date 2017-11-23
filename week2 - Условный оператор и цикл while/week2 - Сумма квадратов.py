# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:18:08 2017

author: Maria Zorkaltseva
"""

# По данному натуральном n вычислите сумму 1²+2²+3²+...+n².

n = int(input())
Sum = 0
i = 1
while i <= n:
    Sum = Sum + i**2
    i = i + 1
print(Sum)
