"""
练习3：输入三条边长，如果能构成三角形就计算周长和面积。

Ver: 0.1
Author: JT
Date: 02/05/2020
"""

import math

side1 = float(input('Please enter the lenth of the first side:'))
side2 = float(input('Please enter the lenth of the second side:'))
side3 = float(input('Please enter the lenth of the third side:'))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print('The parameter of the triangle is %.3f, and the area is %.3f.' \
          % (side1 + side2 + side3, sqrt(side1 ** 2)))
else:
    print('It is not a triangle.')