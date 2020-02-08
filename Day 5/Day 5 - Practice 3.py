"""
3.输出100以内所有的素数。
说明：素数指的是只能被1和自身整除的正整数（不包括1）。

Ver: 0.1
Author: JT
Date: 02/07/2020
"""

num = 1
while num < 100:
    num += 1
    factor = 2
    while factor < num:
        if num % factor == 0:
            break
        factor += 1
    if num == factor:
        print(num, end=' ')
print()