# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:08:09 2017

author: Maria Zorkaltseva
"""

# Для данного числа n<100 закончите фразу “На лугу пасется...” 
# одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, 
# правильно склоняя слово “корова”.

n = int(input())
if 11 <= n <= 14:
    print(n, 'korov')
elif n % 10 == 1:
    print(n, 'korova')
elif (n % 10 == 0) or (5 <= n % 10 <= 9):
    print(n, 'korov')
elif (2 <= n % 10 <= 4):
    print(n, 'korovy')
