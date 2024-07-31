"""
Time Complexity -> O(n log n)  (best/Average case)
Time Complexity -> O(n^2) (Worst Case)
Space Complexity -> O(1)
"""

"""
	The function is called with the parameters:
	quickSort(input, 0, size - 1);

"""
from typing import List


def quickSort(arr: List[int], startIndex: int, endIndex: int):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while (
                arr[i] <= pivot and i < high
            ):  # Changed from `i <= high - 1` to `i < high`
                i += 1

            while (
                arr[j] > pivot and j > low
            ):  # Changed from `j >= low + 1` to `j > low`
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quick_sort(arr, low, high):
        if low < high:
            p_index = partition(arr, low, high)
            quick_sort(arr, low, p_index - 1)
            quick_sort(arr, p_index + 1, high)

    quick_sort(arr, startIndex, endIndex)
