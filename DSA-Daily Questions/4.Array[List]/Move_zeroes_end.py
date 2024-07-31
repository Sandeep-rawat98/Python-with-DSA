##Brute force

from typing import List

"""
Time Complexity = O(N), N is length of array
Space Complexity: O(N)  ## for extra variable we are using temp, and temp will increase as N increase
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        temp = []

        # Copy non-zero elements from original to temp array
        for i in range(n):
            if nums[i] != 0:
                temp.append(nums[i])

        # Number of non-zero elements
        nz = len(temp)

        # Copy elements from temp to fill first nz fields of original array
        for i in range(nz):
            nums[i] = temp[i]

        # Fill the rest of the cells with 0
        for i in range(nz, n):
            nums[i] = 0


## Optimal

"""
Time Complexity = O(N), N is length of array
Space Complexity: O(1)  ## for extra variable we are using temp, and temp will increase as N increase
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                break
            i += 1
        j = i + 1
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
