"""
练习3：输入年份判断是不是闰年。

According to timeanddate.com:
    In the Gregorian calendar, three criteria must be taken into account to identify leap years:
        1. The year can be evenly divided by 4;
        2. If the year can be evenly divided by 100, it is NOT a leap year, unless;
        3. The year is also evenly divisible by 400. Then it is a leap year.

Ver: 0.1
Author: JT
Date: 02/04/2020
"""
y = int(input('Please enter the year: '))
t1 = bool(y % 4 == 0) # test first criteria
t2 = bool(y % 100 == 0) # test second criteria
t3 = bool(y % 400 == 0) # test third criteria
conclusion = bool((t1 and not t2) or t3) # if the year is loop year, the value will be true
print('It is', conclusion, 'that the year is a loop year.')