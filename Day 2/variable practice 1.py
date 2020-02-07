"""
练习1：华氏温度转换为摄氏温度。
提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) div 1.8$。

Ver: 0.1
Author: JT
Date: 02/04/2020
"""
temp = float(input('Please enter your temperature in Fahrenheit: '))
print('Your temerature in Celsius is %.2f.' % ((temp - 32) / 1.8))