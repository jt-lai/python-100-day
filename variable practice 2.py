"""
练习2：输入圆的半径计算计算周长和面积。

Ver: 0.1
Author: JT
Date: 02/04/2020
"""
π = 3.141592657586264 # define π
r = float(input('Please enter the radious: '))
d = 2 * π * r # calculate dimention
a = π * r ** 2 # calculate area
print('The dimention is %.2f, and the area is %.2f.' % (d, a))