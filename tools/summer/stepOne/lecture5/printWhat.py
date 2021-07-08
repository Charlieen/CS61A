"""
What would python print out ?
every function is a kind of patten which control the special behavior.
"""
from operator import add

def square(x):
    return x*x

def delay(arg):
    print("delay")
    def real():
        return arg
    return real

print(delay(delay)()(10)() )

# assert delay(delay)()(10)() ==10

delay(print)()(10)

print(delay(print)()(10))

# variable is found by local, if at the current local, it can be find then stop seeking,
# otherwise , go to his parent scope to seek
def pirate(arggg):
    print("matey",arggg)
    def plunder(arggg): # since the param name is as same as the out layer's param ,
        print(arggg)   # #the out layer param will be overload by local param.
        return arggg
    return plunder

# test1 = pirate(10)
# assert test1(2) ==2

# assert add(pirate(3)(square)(3),1) == 10

# pirate(pirate(pirate))(5)(7)
# assert pirate(pirate(pirate))(lambda x:x+1)(7) ==8



def f_out(arg1):
    print(arg1)
    def f_in(arg2):
        print(arg2+arg1)
        return arg2+arg1
    return f_in


# assert f_out(100)(10) == 110
"""
1: no type could lead to feel confused    
2: no type : meaning name can be refer to any type (must be object, all type is object in python)
3: same name : the ruler is the most nearest, in the same layer from up to down,
4:  
"""
def horse(mask):  # 1: horse is function  r1=> mask is #2
    horse = mask  # r2 => horse is a name pointing to #2
    def mask(horse):    # 1.1 mask is a function(just return his param) ,and has param named horse ,
        return horse        #  1.1.0 mask just return the param which is  recieved in param
    return horse(mask)  # 1.2 this line is the return statement of #1   r3 => horse is pointing r2 , mask pointing #1.1

mask = lambda horse:horse(2)   # 2: mask is function (type is lambda, lambda present: one function,and return apply it with 2 )

horse(mask)  # 3: apply function horse  with mask , called the function.

assert horse(mask) ==2


