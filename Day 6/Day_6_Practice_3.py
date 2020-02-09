"""
练习3：实现判断一个数是不是素数的函数。

Ver: 0.1
Author: JT
Date: 02/08/2020
"""

def is_prime(num):
    factor = 2
    while factor < num:
        if num % factor == 0:
            return True
        factor += 1
    return False