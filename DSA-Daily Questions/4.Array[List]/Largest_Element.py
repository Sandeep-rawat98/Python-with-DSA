## brute force

"""
TC - O(N log N)
SC- O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr: [], n: int) -> int:

    arr.sort()

    # Return the largest from the end
    return arr[-1]


## Optimal
"""
Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

from sys import *
from collections import *
from math import *


def largestElement(arr: [], n: int) -> int:
    max_num = arr[0]  ## largest = float("-inf")
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num


### or better to remove if else
def largestElement(arr: [], n: int) -> int:
    max_num = arr[0]  ## largest = float("-inf")
    for num in arr:
        maxi = max(maxi, arr[i])
    return max_num
