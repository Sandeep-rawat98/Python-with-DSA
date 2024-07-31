class Solution:
    def fib(self, n: int) -> int:
        num = n
        if num <= 1:
            return num
        return fib(num - 1) + fib(num - 2)
