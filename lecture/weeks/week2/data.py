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

# assert 2 in [1,2,3] == True

print(2 in [1,2,3])

assert (2 in [1,2,3]) == True
assert (10 not in [1,2,3]) == True
# assert 10 not in [1,2,3] == True
# Slicing
#         0 1 2 3 4 5 6 7 8 9
demoData=[1,2,3,4,5,6,7,8,9,10]
print(demoData[1:3])
assert demoData[1:3]==[2,3]
assert demoData[1:3:1]==[2,3]
print(demoData[0:6:2])
# assert demoData[0:6:2]==[0,2,4]
print('------207---line--------')

# Trees
# one_two = [1,2]
# nested =[[1,2],[],[[3,False,None],[4,lambda:5]]]
#
def tree(root_label, branches_=[]):
    if len(branches_)==0:
        return [root_label]
    else:
        for branch in branches_:
            assert is_tree(branch), 'branches must be tree'
            return [root_label] + list(branches_)

def label(tree):
    return tree[0]

def branches(tree):
    if type(tree) == int:
        return False
    else:
        return tree[1:]


# [[]],
def is_tree(tree):
    if type(tree) !=list or len(tree)<1: # make sure all element(in tree) was in list
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)


def fib_tree(n):
    if n==0 or n==1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n,[left,right])

def count_partitions(n,m):
    print(n,m)
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m+without_m


def parti_tree(n,m):
    if m==0 or n<0:
        return tree(False)
    elif n==0:
        return tree(True)
    else:
        with_m, without_m = parti_tree(n-m,m), parti_tree(n,m-1)
        return tree(m,[with_m,without_m])

parti_tree_1= parti_tree(3,2)
# [2, [2, [False], [1, [True], [False]]], [1, [1, [1, [True], [False]], [False]], [False]]]
# print(parti_tree_1)

def print_partis(tree,partition=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(partition))
    else:
        left,right = branches(tree)
        m = str(label(tree))
        print_partis(left,partition+[m])
        print_partis(right,partition)

print_partis(parti_tree(6,4))

#tree=[tree[1:],tree[0]]
# 高度的技巧，
def right_binarize(tree):
    if is_leaf(tree):
        return tree+100
    if len(tree) > 2:
        tree = [tree[0], tree[1:]]
    return [right_binarize(b) for b in tree]

demo_right_binarize = right_binarize([1,2,3,4,5,6])

print(demo_right_binarize)

def gen(n):
    if n%2==0:
        return n
    else:
        return [n]
test_1=[gen(c) for c in [1,2,3,4] ]
test_2 =(2*c for c in [1,2,3])


#print(test_1)





# fib_tree_2 = fib_tree(4)
#
# print(fib_tree_2)




#[1, [2, [21], [22]], [3, [31], [32]], [4, [41], [42]]]
# nestedTree_1= tree(1,[tree(2,[tree(21),tree(22)]),tree(3,[tree(31),tree(32)]),tree(4,[tree(41),tree(42)])])
# print(label(nestedTree_1[]))
#
# print(nestedTree_1)


# tree demo [3,[1,[]]]

# print(type(tree))


# t= tree(3,[tree(1),tree(2,[tree(1),tree(1)])])
# print(t)
# t = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
# print(t)


# test=[1]
# print(test[1:])
#
# print(not [])
# print(not [1])
#
#
# # [2,[[1],[1]]
# tree_demo_1 = tree(2,[tree(1),tree(1)])
#
# print(tree_demo_1)
#
# print(label(tree_demo_1))
# print(branches(tree_demo_1))
# print(is_tree(branches((tree_demo_1))))
#
#
# tree_demo_2 = tree(1)
#
# print(tree_demo_2)
# print(is_tree(tree_demo_2))
# print(is_leaf(tree_demo_2))
#
# print(len([[[]]]))
#
# print(is_tree([[]]))
#
# test_empty_1=[]
# print(test_empty_1[1:])
#
