from typing import List


def reverseArray(n: int, nums: List[int]) -> List[int]:
    def reverse(arr, start, end):
        if start >= end:
            return arr
        arr[start], arr[end] = arr[end], arr[start]
        return reverse(arr, start + 1, end - 1)

    return reverse(nums, 0, n - 1)
