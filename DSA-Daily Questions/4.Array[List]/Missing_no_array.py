###Brute force approach

## TC - O(N**N), SC-O(1)


def missing(nums: list):
    for i in range(0, len(nums)):
        if i not in nums:
            return i


print(missing([1, 0, 4, 3]))


### Better force approach

from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""

from typing import List


def missingNumber(nums: List[int]) -> int:
    freq = {i: 0 for i in range(0, len(nums) + 1)}
    for i in nums:
        freq[i] += 1
    for k, v in freq.items():
        if v == 0:
            return k


print(missingNumber([1, 0, 4, 3]))


### Optimal approach

from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""

from typing import List


def missingNumber1(nums: List[int]) -> int:
    n = len(nums)
    original_total = (n * (n + 1)) // 2
    return original_total - sum(nums)


print(missingNumber1[0, 1, 4, 5, 3])
