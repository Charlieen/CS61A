import math
from operator import mul
""" try to use high order function to show the idea of 
Generalizing Patterns with Argument
Regular geometric shapes relate length and area.
    1*r*r, pi* r*r,
    
The Common structure among functions may be a computational process, 
rather than a number.
    
"""

# 1: r*r

def squareForArg(r):
    assert r>0, 'A length must be positive'
    return r*r

def combine(constArg,r,f=squareForArg):
    return constArg * f(r)

def combine2(begin,end,f):
    result= 0.0
    for x in range(begin,end+1):
        temp = f(x)
        result += temp
    return result


def lengthAndAreaFactory(typeName,coreArg):
    if typeName == 'square':
        return combine(1,coreArg)
    elif typeName == 'circle':
        return combine(math.pi,coreArg)
    elif typeName == 'sixSquare':
        return combine(math.sqrt(3)*3/2,coreArg)
    elif typeName =='SumK':
        return combine2(1,coreArg,lambda x:x)
    elif typeName == 'SumKKK':
        return combine2(1,coreArg,lambda  x: x*x*x)
    elif typeName =='SumComplex':
        return combine2(1,coreArg,lambda x: 8/mul(4*x-3,4*x-1))
        #return combine2(1,coreArg,lambda  x: 8/((4*x-3)*(4*x-1)))


demo1 = lengthAndAreaFactory("circle",2)
demo2 = lengthAndAreaFactory("SumComplex",50000000)
print(demo1)
print(demo2)

