def fib(num):
    if num <= 1:
        return num
    return fib(num - 1) + fib(num - 2)


print(fib(4))


class Solution:
    def fib(self, n: int) -> int:
        num = n
        if num <= 1:
            return num
        return fib(num - 1) + fib(num - 2)


###coding ninja
from typing import List


def generateFibonacciNumbers(n: int) -> List[int]:
    fib_numbers = [0, 1]
    for i in range(2, n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers[:n]
