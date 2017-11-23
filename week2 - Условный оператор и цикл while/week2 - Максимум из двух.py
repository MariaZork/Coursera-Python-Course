# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:04:07 2017

author: Maria Zorkaltseva
"""

# Напишите программу, которая считывает два целых числа A и B 
# и выводит наибольшее значение из них. Числа — целые от 1 до 1000.

A = int(input())
B = int(input())
if A > B:
    max = A
elif B > A:
    max = B
else:
    max = A
print(max)