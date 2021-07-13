"""
without the cache mechanism
"""
def fib(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

"""
with cache mechanism
"""
cf={}

def fib_r(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return cache(fib_r,n-2,cf)+cache(fib_r,n-1,cf)



def cache(f,n,cf):
    if n in cf.keys():
        return cf.get(n)
    else:
        cf[n]= f(n)
        return cf.get(n)


print(fib_r(200))




