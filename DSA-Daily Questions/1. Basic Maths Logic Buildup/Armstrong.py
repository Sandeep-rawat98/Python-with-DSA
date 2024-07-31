def checkArmstrong(n):
    num = n
    num_digits = len(str(n))
    total = 0
    while num > 0:
        digit = num % 10
        total =total+ digit ** num_digits
        num //= 10
    return total == n

print(checkArmstrong(153))
