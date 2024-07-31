"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(1)
"""


def countMax(arr: list):
    count = 0
    maxi = 0
    n = len(arr)
    for i in range(0, n):
        if arr[i] == 1:
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    return max(maxi, count)  ### if at last arrat we have 1 and not 0 for that edge case


print(countMax([1, 1, 0, 1, 1, 1]))
