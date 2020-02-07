
"""
练习3：打印如下所示的三角形图案。

*
**
***
****
*****
    *
   **
  ***
 ****
*****
    *
   ***
  *****
 *******
*********

Ver: 0.1
Author: JT
Date: 02/06/2020
"""

x = int(input('Please choose the shape of triangle [1, 2, or 3]: '))

# shape 1
if x == 1:
    for i in range(1, 6):
        while i != 0:
            print('*', end='')
            i -= 1
        print()

# shape 2
if x == 2:
    for i in range (1, 6):
        j = 5 - i
        while j != 0:
            print(' ', end='')
            j -= 1
        while i != 0:
            print('*', end='')
            i -= 1
        print()

# shape 3
if x == 3:
    for i in range (1, 6):
        j = 5 - i
        i = i * 2 - 1
        while j != 0:
            print(' ', end='')
            j -= 1
        while i != 0:
            print('*', end='')
            i -= 1
        print()