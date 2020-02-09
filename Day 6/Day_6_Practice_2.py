"""
练习2：实现判断一个数是不是回文数的函数。
From Wikipedia: A palindromic number is a number that remains the same 
    when its digits are reversed.

Ver: 0.1
Author: JT
Date: 02/08/2020
"""

def is_palindromic(num):
    # reverse number
    temp = num
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    
    # decision
    return num == reversed_num