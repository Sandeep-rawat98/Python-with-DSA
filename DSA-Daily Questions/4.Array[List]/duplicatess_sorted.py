### Brute force

from typing import List

"""
Time complexity = O(n) where n is the number of elements in list
We are looping two different times, so it will be O(n) + O(n).
Which equals tos O(n)

Space complexity = O(n), suppose all numbers are unique, it will take same length as list
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        my_dict = dict()
        for i in nums:
            my_dict[i] = 0

        j = 0
        for n in my_dict:
            nums[j] = n
            j += 1
        return j


## optimal Solution


def removeDuplicates(arr, n):
    # Check if the array is empty or has only one element
    if len(arr) == 1:
        return 1
    i = 0
    n = len(arr)
    j = i + 1

    while j < n:
        if arr[j] != arr[i]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1
    return i + 1


def reverse_array(array: list, start: int, end: int):
    arr = list
    n = len(array)
    i = start
    j = end
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


reverse_array([55, 31, 67, 89, 1, 99, 35], 0, 5)
