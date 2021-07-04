"""
How to try to find the reversion value
Ex: square(4)= 16  => sqrt = reversion(square)  sqrt(16) => 4
how to implement this process ?
"""

def search(f):
    x=0
    while True:
        if f(x):
            return x
        else:
            x+=1

def isThree(x):
    return x==3


def square(x):
    return x*x

# print(search(square))

#  y is function like square  => reversion(square) => sqrt()
#  find reversion function.
#
def reversion(y):
    return lambda x: search(lambda x:y(x))

"""
  problem: known: square(25)= 625 => how to write a general function to implement reversion 
    goal1: from square =>  reversed function : sqrt
    goal2: using sqrt and search implement known 625 and square then we can find 25.
  process:
   1: how to resolve reversed function : from the math view.
      normal function: f,  f(x) =y  => y = f(x)   { apply function g to two sides of the equation} then 
      =>:
          reversed function:            g(y) = g(f(x)) :  =>  finally => value 
      
   2: transform into python :
        - write a function whose param is "f" ,and it return a function which  represents  g(y)
        -  using search to find the y according the result : f(x)== y  {this is the essential process of reversed functions} 
"""
# what is wonderful the code to present the process of acquiring the reversed function and get the resolve.
def reverse(f):
    return lambda y: search(lambda x: f(x) == y)

sqrt = reverse(square)

print(type(sqrt))
print(sqrt(625))


