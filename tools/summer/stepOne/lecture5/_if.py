def if_(c,t,f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """ The real part of the square root of X"""
    if x>0:
        return sqrt(x)
    else:
        return 0.0

"""
    before the function was called,  all the params are evaluated first.
"""
def real_sqrt_2(x):
    return if_(x>0, sqrt(x),0.0)

# real_sqrt_2(-2)

def reasonable(x):
    return x==0 or 1/x;

print(reasonable(11110))

def conditionalExpression(x):
    return abs(1/x if x!=0 else 0)


print(conditionalExpression(90))

print(conditionalExpression(0))

