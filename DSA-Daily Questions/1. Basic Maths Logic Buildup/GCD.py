"""
TC- O(N)
"""

# def calcGDC(n:int, m: int) -> int:
#     if n > m:
#         mn = n
#     else:
#         mn = m
#     for i in range(1, mn+1):
#         if (n%i ==0) and (m%i==0):
#             hcf = i
#     return hcf

"""
The time complexity of the Euclidean algorithm for finding the greatest common divisor (GCD) is typically expressed as O(log(min(n, m))).
"""


def calcGDC(n: int, m: int) -> int:
    while m:
        n, m = m, n % m
    return n
