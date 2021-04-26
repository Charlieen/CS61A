def f1(n):
    def f2(m):
        return m+n
    return f2

demo_1= f1(10)
print(demo_1(9))

increment = lambda x: x + 1

# def make_repeater(f,n):
#     def f2(m):
#         print('can get n from here? ',n,f)
#
#         return f(n)+m
#     return f2
#
# demo1=make_repeater(square,5)
#
# print(type(demo1))
# print(demo1(3))
square = lambda x: x * x

# 1:f2 in the make_repeater so in f2  f and n can be seen which means that f and n can be use ,for example: print(n)
# However,if in f2 , there is "n>0" ,  "n" at the left of operators, n will be looked as param
# UnboundLocalError: local variable 'i' referenced before assignment
def make_repeater(f, n):
    def f2(m):
        total=m
        i=n # i is local variable of f2, and n is the param coming from outer function  make_repeater
        #n=100 this will make python confuse, here n as a local varible which will confic with n from the outer funcion
        while i>=1:
            total =f(m)
            m= total
            i=i-1
        return total
    return f2

demo1= make_repeater(square,2)
print(demo1(5))

# i
def test_while(i):
    while i>10:
      #  print(i)
        i=i-1

test_while(13)

# def test_while_2(i):
#     def inner_(n):
#         while i>10:
#             print(i)
#             i=i-1
#             print(n)
#             n=n+1
#         return n
#     return inner_
#
# demo_2_1= test_while_2(9)
#
# print(demo_2_1(10))

# """Return the function that computes the nth application of f.
#      >>> add_three = make_repeater(increment, 3)
#      >>> add_three(5)
#      8
#      >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
#      243
#      >>> make_repeater(square, 2)(5) # square(square(5))
#      625
#      >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
#      152587890625
#      >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
#      5
#      """

def accumulate(combiner, base, n, term):
    total, i = base, n
    while i >= 1:
        total = combiner(total, term(i)) # term error: function called layer is wrong
        # total = combiner(total, term)  # term error: function called layer is wrong
        # total = combiner(total, term(11))  # ok: this layer is no real calculate,the calculation is in outer layer
        i = i - 1
    return total

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h
# accumulate(combiner, base, n, term):
# compose1(lambda x:accumulate(lambda x,y:compose1(f,f) ,x,n,lambda x:x),lambda x:x)

# """compose1:  Return a function h, such that h(x) = f(g(x))."""
# From the abstraction, this function has covered all the parts:
#  1: the map from one value to another value : term = function
#  2: the accumulate base, and times :n
#  3: how to accumulate : combiner
# So I can know that the  accumulate function can be use to express the repeat function.
#  s1: this is from a general abstraction to a special abstraction
#  s2: need to evaluate whether the space of resolve can cover the question space.
#  s3: in the essential core operators are  multi-times use f(g(x))
#  s4:

# def accumulate(combiner, base, n, term):
#     total, i = base, n  # one time assignment
#     while i >= 1:    # the repeat parts are here,  f(g(x))
#         total = combiner(total, term(i))  # here compose1 will be combiner so total =f,term(i)=g
#         i = i - 1
#     return total

# 1:  layer one  build well the framework:
#       repeat  f(g(x)) n times and f= lambda x:x then prepared to
#        just depend on the g accumulate to use pre result
#      in this layer one  the x present:
#
#       a)during the process of iterators,the outer function f is lambda x:x
#         x is the middle process results

# 2:  layer two , there is only one function which was left,square, the x also coming from two
#      types:
#        a): first, y coming from the init params (the final called repeat_demo(2))
#        b): total = combiner(total, term(i))  total =>lambda x:x, term(i) => lambda x:f
#                     combiner => f(g(x))
#        c):
#
def repeat(f,n):
    return accumulate(compose1,lambda x:x,n,lambda y:f)

#                           1 f(one layer)  2 g(two layers)
#  1 accumulate(compose1,lambda x:x,n,lambda y:f)# f = square = lambda x:x*x
#   a):repeat_demo = repeat(square,3)  is the layer - 1 , the output is a function in which including another
#    function lambda y:f  <=> g  in this process, the 1 f have been consumed and the 2 g have left
#    the last one layer which will be used when  repeat_demo(2) was  called.
#     in the g ,  y has been consumed , even not real calculate to see line 81
#   b): repeat_demo(2)  the real run is  lambda x: x*x , the x receive the final param 2 ;

#
repeat_demo= repeat(square,2) # term(i) = square(x)
print(type(repeat_demo))
print(repeat_demo(2))




# Question:  0: all in all, the function will receive a argument and a function and a count,
# Question:  1: do function(argument) count times, and make sure the output will be the next round input
# Solution:  1: how to resolve the output will(function) be the next round input(function)
#            1.1: high order function  h(x)=f(g(x)) composited functions and assignment operators
#            1.2: how to repeat count times => use while
#
def repeat_2(f,n):
    g = lambda x:x  # operator's left variable's type depend on the right side evaluations
    while n > 0:
        g = compose1(f, g) # high order function and assignment operations
        n = n - 1 # repeat
    return g  # return the function callable




