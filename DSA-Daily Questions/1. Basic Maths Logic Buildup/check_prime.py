from math import *
from collections import *
from sys import *
from os import *


## Read input as specified in the question.
## Print output as specified in the question.
def checkPrime(num: int) -> int:
    if num == 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if checkPrime(int(input())):
    print("YES")
else:
    print("NO")


"""
Sum of all Divisors
"""

"""
Brute force
"""


def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                Sum += j
    return Sum


"""
Better

"""

import math


def sumOfAllDivisors(n: int) -> int:
    Sum = 0
    for i in range(1, n + 1):
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                Sum += j
                if i // j != j:
                    Sum += i // j
    return Sum


""""
Optimal
TC-O(N)
SC-O(1)
"""


def sumOfAllDivisors(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i * (n // i)
    return sum
