import math
"""
HOF
1: for example, I want to do one goal which is add two numbers, the first number must is positive,and the second
number must is negative and abs(second number)> first number.
    - two steps, and second step depend on the result of the first step.
    - the first step will be certainly and then the second step can evaluate according the result of the first step.
* Express general methods of computation
* Remove repetition from program
* Separate concerns among functions.    
"""
def make_add(n):
    """Return a function that take one param and return
    a new function K and then return K+N

    >>> add_three = make_add(3)
    >>> add_three(-4)
    -1
    """
    assert n>0,'outside layer just accept positive number'
    def inner(m):
        """ A local def statement
        here the good thing is where can access the outside variables
            can refer to names in the enclosing functions
        """
        assert m<0 and abs(m)>n,'inner layer just accept negative number and abs value great than outside numbers'
        return n+m
    return inner

add_one = make_add(4)

print(add_one(-2))

