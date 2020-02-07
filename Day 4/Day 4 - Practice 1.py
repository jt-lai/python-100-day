"""
练习1：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数。

Ver: 0.1
Author: JT
Date: 02/06/2020
"""

i = int(input('Please enter a positive integer: '))
denominator = 1
while denominator != i:
    denominator += 1
    if i % denominator == 0 and denominator != i:
        print('The number is NOT a prime number.')
        break
if denominator == i:
    print('The number is a prime number.')