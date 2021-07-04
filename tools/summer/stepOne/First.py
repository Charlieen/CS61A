from datetime import datetime
""" this is for the fib function
    0,1,1,2,3,5,8,13
    1: get the nth number
    2: get the list until nth numbers,
"""

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

def fib_iterator(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        pre2,pre1 = 0,1
        while n>1:
            temp= pre2+pre1
            pre2 = pre1
            pre1 = temp
            n=n-1
        return pre1

def test_fib_it(n):
    for x in range(0,n):
        print(fib_iterator(x))


def getAllFibNumByRange(n):
    for x in range(0,n):
        print(fib(x))

print(datetime.now().microsecond)
test_fib_it(400)
#getAllFibNumByRange(40)
print(datetime.now().microsecond)