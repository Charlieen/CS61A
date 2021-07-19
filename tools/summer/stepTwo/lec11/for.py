from operator import add
def count(s,value):
    """ count the number of times which value appear in the s sequence
    >>> count([1,2,2,3],2)
    2
    >>> count([1,2,2,[2,2],3],2)
    4
    """
    total,index =0,0
    while index <= len(s)-1:
        if s[index] == value:
            total +=1
            index +=1
        else:
            index+=1
    return total

# assert count([1,2,2,3],2) == 2


def count_r(s,value):
    total,index =0,0
    while index <= len(s)-1:
        if isinstance(s[index],int):
            if s[index] == value:
                total,index = total+1,index+1
            else:
                index +=1
        elif isinstance(s[index],list):
            return total+ count_r(s[index],value)
    return total

assert count_r([1,2,2,[2,2,[2,3,[2,10]]],3],2) == 6

print(count_r([1,2,[3,2,[4,2,[5,2,[6,2]]]]],2))


def count_for(s,value):
    total =0
    for v in s:
        if v == value:
            total +=1
    return total

pairs =[[1,[2,9],9],[2,2,9],[1,3,9],[3,3,8]]



def demo(pairs):
    same_count = 0
    for x, y,z in pairs:
        print(x,y,z)
        if x == y:
            same_count = same_count + 1
    return same_count

assert demo(pairs) == 2

def sum_below(n):
    l =list(range(1,n))
    total =0
    for m in l:
        total +=m
    print(total)
    return total

sum_below(100)

def list_comprehence():
    letters=['a','b','c','d','e','f']
    t =[letters[i] for i in range(4)]
    odds=[1,3,5,7,9]
    t2= [x for x in odds if 25% x ==0]
    print(t2)
    print(t)

list_comprehence()

def divisors(n):
    return [1]+[x for x in range(2,n) if n % x ==0]

print(divisors(40))

def string_abstraction():
    # curry= lambda x:x
    # temp ='curry=lambda f: lambda x:lambda y: f(x,y)'
    # exec(temp)
    # assert curry(add)(10)(100) == 110

string_abstraction()

