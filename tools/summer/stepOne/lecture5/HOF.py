def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x*x

# print(apply_twice(square,2))

def apply(f,x):
    while f(x)!= x:
        x=f(x)
    return x

def g(x):
    return (x+5)//3

# print(apply(g,5))

def square(x):
    return x*x
def triple(y):
    return 3*y

def composite1(f,g):
    def h(x):
        return f(g(x))
    return h

firstTripleAndSquare = composite1(square,triple)

firstSquareAndTriple = composite1(triple,square)


print(firstTripleAndSquare(4))
print(firstSquareAndTriple(4))

def search(f,n):
    if f(n):
        return 'yes'
    else:
        return 'no'



