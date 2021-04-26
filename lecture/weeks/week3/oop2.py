from datetime import date
tues = date(2021,3,23)
print(repr(tues))
print(str(tues))
print(tues.__repr__()) # the repr function always invokes __repr__ on its argument
print(tues.__str__()) #

class Account:
    def __init__(self,name,amount):
        self.name=name
        self.amount = amount

    def __bool__(self):
        return self.amount >=3000

    def __repr__(self):
        return 'name has '+self.name + str(self.amount)

    def __str__(self):
        return 'name: '+ self.name+', amount is: '+ str(self.amount)


charlie = Account('charlie',2000)

print(charlie)
print(bool(charlie))

assert len('charlie') == 7

assert 'charlie'.__len__() ==7

assert bool('')==False
assert bool([]) ==False
assert bool('charlie') == True

assert 'charlie'.__getitem__(3)=='r'
assert 'charlie'[3] =='r'

def make_adder(n):
    def adder(k):
        return n+k
    return adder

add_3=make_adder(3)
assert add_3(7) == 10

class outer_class:
    def __init__(self,n):
        self.n=n
    def inner_class(self):
        ref=self
        class inner_class:
            def __init__(self,m):
                self.m=m
            def add(self):
                return self.m+ ref.n
        return inner_class

o= outer_class(3)

assert o.inner_class()(4).add() ==7

class Adder(object):
    def __init__(self,n):
        self.n =n
    def __call__(self,k):
        return self.n+k

class Adder2:
    def __init__(self,n):
        self.n =n

a= Adder(10)
assert a(90) ==100  # python interpreter will call Adder __call__() method to execute the a(90)


print(callable(Adder))
print(callable(Adder2))
print(callable('hello'))
print(type('hello'))
print(type(Adder2))
print(type(str))
print(callable(str))

# right and privileges of first-class elements are:
# 1:They may be bound to names
# 2: They may be passed as arguments to functions lambda
# 3: They may be returned as the results of functions
# 4: They may be included in data structures
# Python awards functions full first-class status,and the resulting gain in expressive power is enormous
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
# function name reused
# function definitions, a much more powerful abstraction technique by which a name can be bound
# to compound operation,which can then be referred to as a unit.

# high order function
def count(f):
    def counted(*args):
        counted.count +=1
        return f(*args)
    counted.count=0
    return counted

# fib = count(fib)
#
# print(type(fib))
# fib(5)
# print(fib.count)


def frame_count(f):
    def counted(*args):
        counted.frame_open +=1
        counted.frame_max= max(counted.frame_open,counted.frame_max)
        result = f(*args)
        counted.frame_open -=1
        return result
    counted.frame_max=0
    counted.frame_open=0
    return counted

# fib= frame_count(fib)
#
# print(fib(190))
#
# print(fib.frame_max)

def memo(f):
    cache={}
    def memorize(n):
        if n in cache:
            return cache[n]
        else:
            cache[n]=f(n)
            return cache[n]
    return memorize

# how higher-order functions can serve as powerful abstraction mechanisms,
# vastly increasing the expressive power of our language
# different layer function can handle different steps which are in the process from bottom to top.
fib = memo(fib)
fib = frame_count(fib)


# print(fib(5))
print(fib(150))
print(fib.frame_max)