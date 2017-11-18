# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 03:09:13 2017

author: Maria Zorkaltseva
"""

# Дано трехзначное число. Найдите сумму его цифр.

n = int(input())
a = n % 10
temp = n // 10
b = temp % 10
c = temp // 10
print(a + b + c)
