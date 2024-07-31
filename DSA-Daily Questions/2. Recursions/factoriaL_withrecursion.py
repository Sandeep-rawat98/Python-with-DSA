def fact(num):
    if num == 1 or num == 0:  ### base condition
        return 1
    return num * fact(num - 1)


ans = fact(7)
print(ans)
