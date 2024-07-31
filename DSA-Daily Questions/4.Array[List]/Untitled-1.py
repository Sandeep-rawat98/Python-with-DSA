class Solution:
    def binarySearchLeft(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        index=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                index=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return index
    def binarySearchRight(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        index=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                index=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return index
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ext_left=self.binarySearchLeft(nums,target)
        ext_right=self.binarySearchRight(nums,target)
        return [ext_left,ext_right]


def process_number(n):
    if n % 2 == 0:
        return n // 2  # Use integer division for even numbers
    else:
        return n * 3 + 1  # For odd numbers

# Example usage:
number = 3  # You can change this to any number to test
result = process_number(number)
print(f"Processed number: {result}")





def count_character():
    s = 'sandeep'
    char_count = {}  # empty dict
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print(count_character())
