add_1 = lambda x:x+1

# you can see what is the real idea about he high order function
# 1:the first layer x control which function can be returned
# 2:the second layer x is the practical param to be calculated by the returned fucntion
# which according the first layer x.
# this example demonstrates how the high order function decompose the process which
# include multi-layers in deep.
def add_one(x):
    if x>0:
        return add_1
    return lambda x:add_1(-1*x)

#                  1   2   3
# print(add_one_2(10)(222)(1))
# 1 layer:  output is a lambda(l1)  which include another lambda(l2)
# 2 layer:  output is a lambda (l2) l2's name  is add_1
# 3 layer:  output is the result of add_1 which receive the param (1) and response the result is 1+1 =2
def add_one_2(x):
    return lambda x:add_1   # here add_1 is a lambda


def add_one_2_1(x):
    return lambda x:add_1(x) # here add_1(x) is a function called which must return a value (None or another)



print(add_one(-1)(3))


print(add_one_2(10)(222)(1))

print(add_one_2_1(10)(1))

