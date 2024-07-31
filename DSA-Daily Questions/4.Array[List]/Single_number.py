###TC - O(N), SC-O(N)
##Brute approach


def singleNumber(nums: list) -> int:
    count_dict = {}

    # Count occurrences of each element
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the element with a count of one
    for num in count_dict:
        if count_dict[num] == 1:
            return num


arr = [4, 1, 2, 1, 2]
print(singleNumber(arr))

##Optimal Approach ###TC - O(N), SC-O(1)


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_sum = sum(set(nums))
        total_sum = sum(nums)
        return 2 * unique_sum - total_sum


## Another approach using X-OR
