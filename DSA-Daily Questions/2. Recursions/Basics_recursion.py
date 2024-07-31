def func(i, n):
    if i > n:
        return
    print(i)
    func(i + 1, n)


func(1, 4)


### preint 1 to N
def func1(i, n):
    if i > n:
        return
    print(i)
    func1(i + 1, n)


func1(1, 5)


### print N to 1
def function(n):
    if n < 1:
        return
    print(n)
    function(n - 1)


function(5)

"""
With BACK Tracking

"""


## Print 1 to N without i+1 do with i-1
def function1(n):
    if n < 1:
        return
    function1(n - 1)
    print(n)


function1(5)


## Print n to 1 with i+1
def function2(n):
    if n < 1:
        return
    print(n)
    function2(n - 1)

function2(5)


