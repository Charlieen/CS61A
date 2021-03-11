from fractions import Fraction

print(type(1/3))

def rational(n,d):
    return Fraction(n,d)

# def rational_2(n,d):
#     fractions=[n,d]
#

def numer(x):
    str_x= str(x)
    if str_x.__contains__("/"):
        numerAndDenom= str_x.split("/")
        return numerAndDenom[0]
    else:
        return x

def denom(x):
    str_x = str(x)
    if str_x.__contains__("/"):
        numerAndDenom = str_x.split("/")
        return numerAndDenom[1]
    else:
        return x


frac1= Fraction(11,23337);
print(type(frac1))
print(frac1+1)

# print(numer(frac1))
#
# print(denom(frac1))
#
def add_rationals(x,y):
    nx,dx = numer(x),denom(x)
    ny,dy = numer(y),denom(y)
    return rational(nx*dy +ny*dx,dx*dy)
#
# print(type([]))
# Functions are sufficient to represent compound data
def pair(x,y):
    def get(index):
        if index==0:
            return x
        elif index==1:
            return y
    return get

print(pair(11,22))

def select(p,i):
    return p(i)

# demo

p =pair(11,220)
assert select(p,0)==11
assert select(p,1) ==220

# list
digits =[1,2,3]

compoundList= [20,30] + digits *2

assert compoundList == [20,30,1,2,3,1,2,3]

pairs =[[10,20],[30,40]]

assert pairs[1][1]==40

def count(s,value):
    total,index = 0,0
    while index <len(s):
        if s[index]==value:
            total =total +1
        index = index +1
    return total

# for <name> in <expression>:
#     <suite>

# 1 Evaluate the header <expression>,which must yield an iterable value.
# 2:For each element value in that iterable value,in order:
    # 1:Bind <name> to that value in the current frame
    # 2: Execute the <suite>

def count_for(s,value):
    total=0
    for elm in s:
        if elm==value:
            total =total+1
    return total

paris2=[[1,2],[2,3],[4,5],[6,6]]

def count_(pair):
    same_count = 0
    uptoHigh = 0
    for x, y in paris2: # sequence unpacking
        if x == y:
            same_count = same_count + 1
        elif x < y:
            uptoHigh = uptoHigh + 1
    print(same_count,uptoHigh)


count_(paris2)

# Ranges:
# assert range(1,3)==[1,2]
print(type(range(1,3))) # class range

assert list(range(1,3))==[1,2]
assert list(range(4))==[0,1,2,3]

for _ in range(3):
    print(_)
    print('Go Bears!')

# Sequence Processing

odds = [1,3,5,7,9]

evens= [x+1 for x in odds]
print(128,type(evens))

paris3=(1,2,4,5)

paris3_new =(x+1 for x in paris3)
for _ in paris3_new:
    print(_)

print(type(paris3_new))
print(type((1,2,3,4)))
# assert (x+1 for x in paris3) == (2,3,5,6)

#[<map expression> for <name> in <sequence expression> if <filter expression>]
assert [x for x in odds if x>4] ==[5,7,9]

def divisors(n):
    return [1] + [x for x in range(2,n) if n % x ==0]

print(divisors(12))

perfect_number =[n for n in range(1,1000) if sum(divisors(n))==n]

print(perfect_number)

#assert perfect_number == [6,28,496]

# Higher-Order Functions

def apply_to_all(map_fn,s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn,s):
    return [filter_fn(x) for x in s]

def reduce_(reduce_fn,s,initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced,x)
    return reduced


def divisors_of(n):
    divides_n = lambda x: n % x ==0
    return [1] +keep_if(divides_n,range(2,n))

apply_to_all_2 = lambda map_fn,s: list(map(map_fn,s))

keep_if_2= lambda filter_fn,s: list(filter(filter_fn,s))


assert apply_to_all_2(lambda x:2*x,[1,2,3])==[2,4,6]

assert keep_if_2(lambda x: x % 2==0,[1,3,4,6,7,8])==[4,6,8]

from functools import reduce
from operator import mul

def product(s):
    return reduce(mul,s)

assert product([1,2,3,4,5]) ==120

# Sequence Abstraction length and element selection, membership and slicing

assert 2 in [1,2,3] == True

assert 10 not in [1,2,3] == True


