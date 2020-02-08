"""
2.找出10000以内的完美数。
说明：完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和
    （即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）
    就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。

Ver: 0.1
Author: JT
Date: 02/07/2020
"""

num = 0
while num < 10000:
    num += 1
    sum_factor = 0
    for factor in range(1, num):
        if num % factor == 0:
            sum_factor += factor
    if num == sum_factor:
        print(num, end=" ")
print()