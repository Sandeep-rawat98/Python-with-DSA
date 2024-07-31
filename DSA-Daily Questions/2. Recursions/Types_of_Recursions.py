"""
1.Parametrized
2.Function
"""

"With Parameter"


### print sum of 1 to N
def func(i, sum):
    if i < 1:
        print(sum)
        return
    func(i - 1, sum + i)


func(3, 0)

"With Function"


def func(n):
    if n == 1:
        return 1
    return n + func(n - 1)


ans = func(10)
print(ans)
