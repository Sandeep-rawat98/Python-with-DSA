from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotated = False  # Flag to track if rotation has occurred
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                if rotated:  # If already rotated once, return False
                    return False
                rotated = True  # Mark that rotation has occurred
        return True


### Better Solution
def count(nums: list):
    count_dict = {}
    n = len(nums)  # Define 'n' as the length of the 'nums' list
    for num in nums:
        count_dict[num] = count_dict.get(num, 0) + 1

    for k, v in count_dict.items():
        if v > n // 2:
            return k
    return -1


print(count([3, 2, 3]))
