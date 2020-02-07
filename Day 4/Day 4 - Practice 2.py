"""
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。

Ver: 0.1
Author: JT
Date: 02/06/2020
"""

a = int(input('Please enter a positive integer: '))
b = int(input('Please enter another positive integer: '))

# find the greatest common devisor (gcd)
for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

# find the least common multiple (lcm)
lcm = 0
while True:
    lcm = a + lcm
    if lcm % b == 0:
        break

print('The greatest common divisor of %d and %d is %d.' % (a, b, gcd))
print('The least common multiple of %d and %d is %d.' % (a, b, lcm))