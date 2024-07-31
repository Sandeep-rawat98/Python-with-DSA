def isSorted(n: int, a: [int]) -> int:
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            return 0
    return 1
