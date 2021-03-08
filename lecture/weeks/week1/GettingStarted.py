# from urllib.request import urlopen
#
# shakespeare= urlopen('http://composingprograms.com/shakespeare.txt')
# words= set(shakespeare.read().decode().split())
# somewords={w for w in words if len(w)==6 and w[::-1] in words}
#
# print(somewords)
from operator import mul,add


def square(x):
    return mul(x,x)
print(square(12))
print(square(add(3,3)))
print(square(square(2)))

def sum_squares(x,y):
    """:cvar"""
    return add(square(x),square(y));

print(help(sum_squares))

def fib(n):
    """
    Compute the nth Fibonacci number, for n>=2
    :param b:
    :return:
    """
    pred, curr = 0, 1
    k=2
    while k<n:
        pred, curr = curr, pred+curr
        k=k+1
    return curr

result_fib_8=fib(8)
print(result_fib_8)
# assert fib(8)==15

def fib_test():
    assert fib(2)==1
    assert fib(3)==1
    assert fib(8)==13

fib_test()

def sum_naturals(n):
    """Return the sume of the first n natural numbers
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    total,k=0,1
    while k<=n:
        total,k =total+k,k+1
    return total

from doctest import testmod

testmod()

from doctest import run_docstring_examples
run_docstring_examples(sum_naturals,globals(),True)

# Function as Arguments
def sum_naturals(n):
    total,k =0,1
    while k<=n:
        total,k = total + k ,k+1
    return total

def sum_cubes(n):
    total, k =0,1
    while k<=n:
        total, k = total+k*k*k, k+1
    return total

def summuation(n,term):
    total, k =0,1
    while k<=n:
        total,k = total+term(k),k+1
    return total

def natural(k):
    return k;
summuation_natural = summuation(10,natural);

print(summuation_natural)

def cube(x):
    return x*x*x

cube_sum =summuation(3,cube)

print(cube_sum)

#1.6.2 Function as General Methods

# it doesn't specify what problem is being solved.
# this function is a general expression of repetitive refinement

def improve(update,close,guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess +1

# this is key feature to make sure the result lead to zero, convergence
def suqare_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)

def approx_eq(x,y,tolerance=1e-15):
    return abs(x-y)<tolerance

golden_rate = improve(golden_update,suqare_close_to_successor)

print(golden_rate)


from math import sqrt
phi= 1/2+ sqrt(5)/2
def improve_test():
    approx_phi= improve(golden_update,suqare_close_to_successor)
    assert approx_eq(phi,approx_phi),'phi differs from its approximation'

improve_test()

# Defining Functions Nested Definitions

def average(x,y):
    return (x+y)/2

def sqrt_update(x,a):
    return average(x,a/x)

#  dimension reduction process
#  1) in the real detail subprocess  (update,close ,need two arguments),but improve is easy to handle one argument
#  2) use higher order function and Nested define function can handle this issue.
#  3) high order function need to think carefully the arguments call process.

def sqrt(a): # handle first argument
    def sqrt_update(x): #hanle second argument
        return average(x,a/x) # Critically, the inner functions have access to the names in the environment where they are defined (not where they are called).
    def sqrt_close(x):
        return approx_eq(x*x,a) #hanle second argument
    return improve(sqrt_update,sqrt_close)

sqrt4 = sqrt(4)

print(sqrt4)

#Functions as Returned Values

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def f_g(x):
    return x+10

def f_f(x):
    return 2*x

f_add_10_mul_2=compose1(f_f,f_g)

print(f_add_10_mul_2(10))

assert f_add_10_mul_2(10)==40

# Currying

def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

print(curried_pow(2))
f_pow_2 = curried_pow(2)
f_pow_2_3 = f_pow_2(3)

assert f_pow_2_3 == 8

def map_to_range(start,end,f):
    while start<end:
        print(f(start))
        start=start+1

map_to_range(0,10,f_pow_2)

# we know pow(x,y) pow(2,3)=8
def curry2(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

pow_c= curry2(pow)
pow_c_2=pow_c(2)
pow_c_10=pow_c(10)

assert pow_c_2(3)==8
assert pow_c_10(3)==1000

# nest function , can be used as if you want to solve an issue with many steps ,and each step need different argument and process,
# then you can think about use nest function to handle this scenario.
def uncurry2(g):
    """ Return a two-argument version of the given curried function."""
    def f(x,y):
        return g(x)(y)
    return f

assert uncurry2(pow_c)(10,3)==1000


# Lambda Expressions

def composel1(f,g):
    return lambda x:f(g(x))

addAndMul_1 = compose1(lambda x:x*5,lambda x:x+10)

assert addAndMul_1(90)==500

# Function Decorators
def trace(fn):
    def wrapped(x):
        print('->',fn,'(',x,')')
        return fn(x)
    return wrapped

@trace
def triple(x):
    return 3*x

print(triple(12))



