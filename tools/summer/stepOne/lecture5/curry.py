from operator import add,mul
"""
HOF - curry 
how to use the function to finish these steps.

1: get add
2: get m
3: get n
4: return  add(m,n)
"""
def carry_ex(f):
    def g(x):
        return h
    def h(x):
        return f(g(x),x)
    return h

def carry_final(f):
    def g(x):
        m =x
        def h(x):
            n=x
            return f(m,n)
        return h
    return g

step_1_add = carry_final(add)
step_2_get_10 = step_1_add(10)
step_2_get_10_5 = step_2_get_10(5)

print(step_2_get_10_5)

print(carry_final(mul)(6)(9))


def carry2(f):
    def g(x):
        return x
    def h(x):
        return x
    return f(g,h)



def adder(m):
    def add_two(n):
        return 2+m+n
    return add_two

a=[]
def adder2(m):
    a.append(m)
    def add_three(n):
        return adder2(m+n)
    return add_three

# print(adder(3)(5))

adder2(1)(2)(3)(4)

# print(a)



#

def carry_f(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g

print(carry_f(add)(100)(88))

""" 
using lambda is more simple to express the process of building the process.
"""
def carry_lam(f):
    return lambda x:lambda y: f(x,y)

print(carry_lam(add)(100)(88))

