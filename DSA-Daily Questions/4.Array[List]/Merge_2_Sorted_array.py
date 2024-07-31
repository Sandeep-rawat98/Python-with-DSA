### Brute force approach

"""
Time complexity -> O((n + m) log (n + m))
n is number of elements in a
m is number of elements in b

Space complexity -> O(n+m)
"""


def sortedArray(a: [int], b: [int]) -> [int]:
    freq = set()

    for num in a:
        freq.add(num)
    for num in b:
        freq.add(num)

    return sorted(list(freq))


print(sortedArray([1, 1, 1, 2, 3, 6, 8, 14, 14], [1, 3, 4, 4, 6, 10]))


### Optimal force approach

"""
Time complexity -> O(n+m)
n is number of elements in a
m is number of elements in b

Space complexity -> O(1)
"""


class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, arr1, arr2, n, m):
        # code here
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if len(result) == 0 or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
            else:
                if len(result) == 0 or result[-1] != arr2[j]:
                    result.append(arr2[j])
                j += 1

        while i < len(arr1):
            if len(result) == 0 or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        while j < len(arr2):
            if len(result) == 0 or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        return result
