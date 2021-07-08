def cascade(n):
    if n<10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

# cascade(175)
"""
123
12
1
12
123
how to implement it ?
"""
def cas(n):
    print(n)
    if n>10:
        cas(n//10)
        print(n)

# cas(1234567)
"""
1
12
123
12
1
how to implement it ?
"""
#1
#12
#123

def in_map(i):
    if i==123:
        return 1
    elif i==12:
        return 12
    elif i==1:
        return 123

# try to use str
# def inverse_map(origin,i):
#     count = len(str(origin))+1
#     return int(str(origin)[0,count-len(str(i))])

def apply_num(f,num,n):
    if n ==0:
        return num
    else:
        temp=0
        while n>0:
            temp = f(num)
            num=temp
            n=n-1
        return temp

assert apply_num(lambda x:x//10,123,2) == 1





def inverse_map(origin,i):
    """
    origin =123,when i= 123 =>1, i=12 =>12, i=1 =>123
    """
    count = len(str(i))-1
    return apply_num(lambda x:x//10,origin,count)






def cas_i(n):
    if n<10:
        print(n)
    else:
        cas_i(n//10)
        print(n)

def cas_ii(n):
    index = in_map(n)
    if len(str(index))==3:
        print(index)
    else:
        print(index)
        cas_ii(n//10)
        print(in_map(n))

# cas_ii(123)

####
"""
1
12
123
1234
123
12
1

1：input n=1234 , control process way just using "//" operator,=> 1234,123,12,1  
2: goal: two type print: from small to big and from big to small
3: Analyze: recursive call process include the push stack and pop stack ,which can match the two type print requirement
    -3.1: the total goal can be spited into three parts  1: grow part,1 12 123 ; 2:middle pink 1234 == n; 3: shrink part 123,12,1
    -3.2: the basic inner called mechanical depend on the recursive calling => which can drive the process of calling.
    -3.3: need to depend on the function frame to save the 1,12,123 and the function print, (1234 is the n origin param) 
    -3.4: from 3.3 => design a function f_then_g(f,g,n)  f: recursive function (control process ) g : print n:(1,12,123)
    -3.5: f_then_g main feature is calling the functions( recursive function and print) and control the end of recursive.
    -3.6: the n change depend on the "//"  operator
"""
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f,g,n):
    if n:
        f(n)
        g(n)

grow_1 = lambda  n: f_then_g(f_grow_help, inverse_cascade,n//10)
shrink_1 = lambda  n: f_then_g(inverse_cascade,f_sh_help ,n//10)

grow = lambda n:f_then_g(grow,print,n//10)
shrink =lambda n:f_then_g(print,shrink,n//10)

def f_grow_help(x):
    if x==123:
        return 1
    elif x==12:
        return 12
    elif x==1:
        return 123

def f_sh_help(x):
    if x==12 or x==123:
        return 12
    elif x==1:
        return 1

inverse_cascade(123)





