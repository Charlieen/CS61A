# 18117 = 7+1+1+8+1 =18
# 18117%10 =7 18117 //10 =1811

# this way is just use recursive method to resolve my iterator idea process.
# like translate the figure it out process to code
def sum_digit(n):
    def help_f(total,i):
        if i > 0:
            mid = i // 10
            dig = i % 10
            return help_f(total+dig,mid)
        else:
            return total
    return help_f(0,n)

assert sum_digit(18117) == 18

# real recursive philosophy : begin with the space of the issue resolve,
#
def sum_digit2(n):
    if n<10:  # this is the exit of recursive and the a part of space of resolve
        return n
    else:
        all_but_last,last = n//10, n % 10
        return sum_digit2(all_but_last)+last

sum_digit2(18117)

# 4!= 4* 3*2*1

def fact(n):
    total=1
    index=n
    while index>=1:
        total,index= index*total,index-1
    return total

assert fact(4) ==24

def fact_r(n):
    if n==1:
        return 1
    else:
        return fact_r(n-1)*n

assert fact_r(4) ==24

# Mutual Recursion
# even or odd number,

def is_even(n):
    if n==0:
        return True
    elif is_odd(n-1):
        return True
    else:
        return False


def is_odd(n):
    if n==0:
        return False
    if is_even(n-1):
        return True
    else:
        return False


assert is_even(24) == True






