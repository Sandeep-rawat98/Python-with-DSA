"""
Brute Force
TC - O(n), where n is the number
SC - O(d), where d is the number of divisors of the input integer n
"""

from typing import List


def printDivisors(n: int) -> List[int]:
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result


"""
better

TC - O(n/2)===O(n), where n is the number
SC - O(d), where d is the number of divisors of the input integer n
"""


from typing import List


def printDivisors(n: int) -> List[int]:
    result = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result.append(i)
    result.append(n)
    return result


"""
Optimal
TC - O(sqrt(n) + sqrt(n*logn)) == O(NlogN), where n is the number
SC - O(1), where n is the number
"""
from math import sqrt
from typing import List


def printDivisors(n: int) -> List[int]:
    result = []
    for i in range(1, (int(n**0.5)) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)

    result.sort()
    return result
