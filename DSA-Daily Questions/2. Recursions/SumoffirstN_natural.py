"""
TC - O(N)
SC - O(N)
"""


def sumFirstN(n: int) -> int:
    # Write your code here.
    if n == 1:
        return 1
    return n + sumFirstN(n - 1)


"""
TC - O(1)
SC - O(1)
"""


def sumFirstN(n: int) -> int:
    return (n * (n + 1)) // 2
