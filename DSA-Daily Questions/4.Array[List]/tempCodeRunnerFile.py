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