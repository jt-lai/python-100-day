"""
练习4：写一个程序判断输入的正整数是不是回文素数。

Ver: 0.1
Author: JT
Date: 02/08/2020
"""

def is_prime_and_palindromic(num):
    # figure out if it is palindromic
    temp = num
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    if num != reversed_num:
        return False

    # figure out if it is a prime number
    factor = 2
    while factor < num:
        if num % factor == 0:
            return True
        factor += 1
    return False
    