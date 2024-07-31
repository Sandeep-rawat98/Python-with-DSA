lst = []
list_length = int(input("Enter length = "))
for i in range(list_length):
    num = int(input("Enter number = "))
    lst.append(num)
print(lst)

# Pre compute
hash_list = [0] * 13  # [0,0,0,0,0,0..13 times]
for num in lst:
    hash_list[num] += 1

print(hash_list)
n = int(input("Enter number to count = "))  # 1
print(hash_list[n])  # Fetch


####Dictionary number

lst = [5, 4, 2, 5, 4, 2, 1, 1, 1, 3, 5, 3]

hash_map = {}

# Pre compute
for num in lst:
    hash_map[num] = hash_map.get(num, 0) + 1

print(hash_map)

number = int(input("Enter number to count = "))
print(hash_map.get(number, 0))
