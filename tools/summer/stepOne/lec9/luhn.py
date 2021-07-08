"""
find the check digit from a number by Luhn_algorithm
1: Compute the sum of the sum digits (a ruler)  =>67
2: Multiply by 9  =>603
3: 603 mod 10 is then 3, => X=3
"""
testNumber =79927398710

def doubleThenGet(n):
    temp = 2*n
    if temp > 9:
        first,second = temp//10, temp%10
        return first+second
    else:
        return temp

def getTransformByDigit(d,origin,change):
    origin_str = str(origin)
    change_str = str(change)
    if (len(origin_str)-len(change_str)) %2 !=0:
        return doubleThenGet(d)
    else:
        return d


def sum_digits(n):
    total,flag= 0,0
    while n>0:
        n, pos = n // 10, n % 10
        if flag==0:
            total = total +pos
            flag =1
        else:
            total= total+doubleThenGet(pos)
            flag=0
    return total


def sum_digits_r(n,origin):
    if n<10:
        return getTransformByDigit(n,origin,n)
    else:
        pos = n% 10
        temp = getTransformByDigit(pos,origin,n)
        n = n//10
        return temp + sum_digits_r(n,origin)


assert sum_digits(testNumber) == 67

# assert sum_digits_r(testNumber,testNumber) ==67

print(sum_digits_r(testNumber,testNumber))

def luhn(n):
    sum_n= sum_digits(n)
    return (sum_n *9) % 10

assert luhn(testNumber) ==3

def luhn_r(n):
    origin =n
    sum_n= sum_digits_r(n,origin)
    return (sum_n*9) %10








