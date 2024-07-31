from typing import List


def selectionSort(arr: List[int]) -> None:
    # Write your code here
    n = len(arr)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


"""
Selection sort
Time complexity - O(n^2)
Space complexity - O(1)
"""
