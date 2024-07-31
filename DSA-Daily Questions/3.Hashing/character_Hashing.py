string = "aerrropllane"

char_hash = [0] * 26
print(char_hash)
# Pre store
for ch in string:
    index = ord(ch) - 97
    print(f"this is index: {index}")
    char_hash[index] += 1

print(char_hash)

char = input("Enter char to count = ")
print(char_hash[ord(char) - 97])

##Dictionary  (String)
string = "aeroplllanneee"

hash_map = {}

# Pre compute
for num in string:
    hash_map[num] = hash_map.get(num, 0) + 1

print(hash_map)

number = input("Enter char to count = ")
print(hash_map.get(number, 0))
