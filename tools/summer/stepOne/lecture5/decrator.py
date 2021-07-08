
"""
trace the process of the function
trace1: print out the function name and param before the fn was called
"""
def trace1(f):
    def help(x):
        print('fn is like',f,'param is like',x)
        return f(x)
    return help

@trace1
def square(x):
    return x*x

@trace1
def sum_square_to_n(n):
    total,k=0,1
    while k<=n:
        total,k = total+square(k),k+1
    return total

test = trace1(square)

print(test(3))

assert square(9)==81

sum_square_to_n(5)

