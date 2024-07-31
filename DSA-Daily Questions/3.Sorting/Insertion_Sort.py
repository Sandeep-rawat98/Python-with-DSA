def insertionSort(arr):
    # write your code here !!!
    for i in range(1, len(arr)):  ## i start with 1st index and that will be the key
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


"""
Insertion sort
Time complexity - O(n^2) (Worst and Average)
Time complexity - O(n) (Best case)
Space complexity - O(1)
"""
