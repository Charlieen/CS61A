"""
sum_digits(1234) => 1+2+3+4 = 10
step1: get all digits
step2 : sum

Conditional statement check for base cases
Base cases are evaluated without recursive calls
Recursive cases are evaluated with recursive calls

"""
def sum_digits(n):
    total,digit =0,1
    while n>0:
        digit = n % 10
        total = total + digit
        n= n//10
    return total

assert sum_digits(17234) == 17

def sum_digits_r(n):
    if n<10:
        return n
    else:
        return n % 10 + sum_digits_r(n//10)


assert sum_digits_r(1234) ==10


