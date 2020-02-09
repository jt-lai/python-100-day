"""
练习1：实现计算求最大公约数和最小公倍数的函数。

Ver: 0.1
Author: JT
Date: 02/08/2020
"""

def gcd(a, b):
    # find the greatest common devisor (gcd)
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def lcm(a, b):
    # find the least common multiple (lcm)
    lcm = 0
    while True:
        lcm = a + lcm
        if lcm % b == 0:
            break
    return lcm