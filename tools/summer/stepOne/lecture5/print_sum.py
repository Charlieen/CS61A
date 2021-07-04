def printall(n):
    print(n)
    return printall

# printall(1)(2)(3)

"""

"""
def print_sum(x):
    print(x)
    def printSum(y):
        print(x+y)
        return printSum
    return printSum

# print_sum(1)(2)(3)(4)

def print_adds(x):
    print(x)
    def print_sum(y):
        print_adds(x+y)
        return print_sum
    return print_sum

# print_adds(1)(2)(3)(4)
"""
    continue to add and continue to print out
    1: goals:
        - receive the first param 
        - print the fist value
        - accumulate  second param with first param and print it out
        - continue do this process 
    2: difficult point to implement in python
        - how to pass the value from the inner function to outer function.
            -- return statement plus invoking the outer function
"""
def print_sums(x):  # receive the first param and next accumulated sum param
    print(x)        # print out
    def next_sum(y):  # continue to accept new param to accumulate and print out
        return print_sums(x+y)  # pass the value from inner function to outer function, calling the outer function
    return next_sum  # 1: call the function and finish to continue to accept new param

print_sums(1)(2)(3)
