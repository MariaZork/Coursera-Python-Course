# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 23:11:16 2017

author: Maria Zorkaltseva
"""

# За многие годы заточения узник замка Иф проделал в стене прямоугольное 
# отверстие размером D×E. Замок Иф сложен из кирпичей, размером A×B×C. 
# Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие, 
# если стороны кирпича должны быть параллельны сторонам отверстия.

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A <= D and A <= E or B <= D and B <= E or C <= D and C <= E:
    print('YES')
else:
    print('NO')
