class Tree:
    def __init__(self,label,branches=()):
        for branch in branches:
            assert isinstance(branch,Tree)
        self.label= label
        self.branches= branches

    def __repr__(self):
        rest=''
        if self.branches:
            rest= ', '+ repr(self.branches)
        return 'Tree({0}{1})'.format(str(self.label),str(rest))

    def is_leaf(self):
        return not self.branches

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

print(fib(10))

def fib_tree(n):
    if n==1:
        return Tree(0)
    elif n==2:
        return Tree(1)
    else:
        left_tree= fib_tree(n-2)
        right_tree= fib_tree(n-1)
        return Tree(left_tree.label+right_tree.label,(left_tree,right_tree))

def sum_labels(t):
    def help_(t,acc):
        if type(t) != tuple:
            if t.is_leaf():
                return acc + t.label
            else:
                return help_(t.branches, acc + t.label)
        else:
            return acc

    return help_(t,t.label)

def sum_labels_(t):
    """ Sum the labels of a Tree instance,which may be None"""
    return t.label + sum([sum_labels_(b) for b in t.branches])

fib_5= fib_tree(5)
print(fib_5)
print(sum_labels(fib_5))
print(sum_labels_(fib_5))

def memo(f):
    cache={}
    def memorize(n):
        if n in cache:
            return cache[n]
        else:
            cache[n]=f(n)
            return cache[n]
    return memorize

fib_tree_memo = memo(fib_tree)

sum_labels_memo= memo(sum_labels_)

fib_35 = fib_tree_memo(35)
print(fib_35.label)