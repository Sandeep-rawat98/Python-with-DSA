import math


def countDigits(n: int) -> int:
    return int(math.log10(n)) + 1


print(countDigits(555))


""""
Problem statement
You are given a number ’n’.
Find the number of digits of ‘n’ that evenly divide ‘n’.

Note:
A digit evenly divides ‘n’ if it leaves no remainder when dividing ‘n’.
Example:
Input: ‘n’ = 336
"""


def countDigits(n: int) -> int:
    count = 0
    num = n
    while num > 0:
        digit = num % 10
        if digit != 0 and n % digit == 0:
            count += 1
        num //= 10
    return count
