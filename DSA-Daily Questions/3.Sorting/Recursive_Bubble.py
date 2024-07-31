from typing import List


def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    n = len(arr)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
