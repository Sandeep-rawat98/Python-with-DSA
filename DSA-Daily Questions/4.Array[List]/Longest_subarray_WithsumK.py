## Brute force approach

"""
Time complexity -> O(n^3)
n is number of elements in nums

Space complexity -> O(1)
"""


def longestSubarrayWithSumK(a: int, k: int) -> int:
    n = len(a)

    length = 0
    for i in range(n):
        for j in range(i, n):
            s = 0
            for K in range(i, j + 1):
                s += a[K]
            if s == k:
                length = max(length, j - i + 1)
    return length


## Another brute approach without k loop

"""
Time complexity -> O(n^2)
n is number of elements in nums

Space complexity -> O(1)
"""


# Part 2
def longestSubarrayWithSumK(a: int, k: int) -> int:
    n = len(a)

    length = 0
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += a[j]
            if s == k:
                length = max(length, j - i + 1)
    return length


## Better approach

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""
##Note : this will be the optimal solution if there are(-)ve also


def longestSubarrayWithSumK(a: int, k: int) -> int:
    sum_map = dict()
    Sum = 0
    max_length = 0
    for i in range(0, len(a)):
        Sum += a[i]
        if Sum == k:
            max_length = i + 1

        rem = Sum - k
        if rem in sum_map:
            l = i - sum_map[rem]
            max_length = max(max_length, l)

        if Sum not in sum_map:
            sum_map[Sum] = i

    return max_length

##OPTIMAL

"""
Time complexity -> O(2n) ~ O(N)
n is number of elements in nums

Space complexity -> O(1)
"""

class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        left = 0
        right = 0
        max_length = 0
        Sum = 0
        while right < n:
            Sum += arr[right]
            while Sum > k and left <= right:
                Sum -= arr[left]
                left += 1
            if Sum == k:
                max_length = max(max_length, right - left + 1)
            right += 1
        return max_length
