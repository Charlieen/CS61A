"""
Tree has one root node with label and branches,all the branches are both tree.
"""
def tree(label,branches=[]):
    for b in branches:
        assert is_tree(b),'branches must be tree!'
    return list([label] + branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

# def is_tree(branch):
#     if not isinstance(branch,list) or len(branch)<0:
#         return False
#     else:
#         return is_tree(branch[1:])
#

def is_tree(tree):
    if not isinstance(tree,list) or len(tree)<0:
        return False
    else:
        for branche in branches(tree):
            if not is_tree(branche):
                return False
        return True

def if_leaf(tree):
    return not branches(tree)
"""
how to build a tree like these:
        3
    1       2
         1    1 
"""
def howtoBuildTree():
    node1 = tree(1)
    node2 = tree(1)
    node3 = tree(2,[node1,node2])
    node4 = tree(1)
    node5 = tree(3,[node4,node3])
    print(node5)

howtoBuildTree()

# tree(1,[2])
dtree = tree(3,[tree(1),tree(2,[tree(1),tree(1)])])

print(dtree)

def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
assert  fib(4) == 5


"""
fib_tree(3):
tree(3,[tree(1),tree(2)])
tree(3,[tree(1),tree(2,[tree(1),tree(1)])])

"""
c=[]
def fib_tree(n):
    if n==0 or n==1:
        c.append(tree(1))
        return 1
    else:
        c.append(tree(n))
        return fib_tree(n-2)+fib_tree(n-1)

# fib_tree(3)
# print(c)

def fib_tree_r(n):
    if n ==0 or n==1:
        return tree(n)
    else:
        left,right = fib_tree_r(n-2),fib_tree_r(n-1)
        return tree(n,[left,right])

print(fib_tree_r(5))

# in tree return list([label]+branches)
# list([1] +[2,[3],[4,[5]]]) => [1, 2, [3], [4, [5]]]
# list -> one layer
def fib_tree_f(n):
    if n<=1:
        return tree(n)
    else:
        left,right = fib_tree_f(n-2),fib_tree_f(n-1)
        return tree(label(left)+label(right),[left,right])

all=[]

def count_help(t):
    if if_leaf(t):
        return 1
    else:
        for branch in branches(t):
           all.append(count_help(branch))
        return sum(all)


def count_leaf(t):
    return count_help(t)

tree_fib3 = fib_tree_f(3)

# print(tree_fib)
#
# print(count_leaf(tree_fib))
#
# print(all)


def count_leaf(t,total=0):
    bs = branches(t)
    for branch in bs:
        if if_leaf(branch):
            total +=1
        elif isinstance(branch,list):
            return total + count_leaf(branch,total)
    return total

print(tree_fib3)
print(count_leaf(tree_fib3))


def count_leaf_structure(tree):
    if if_leaf(tree):
        return 1
    else:
        branchesTotal = [count_leaf_structure(branch) for branch in branches(tree)]
        return sum(branchesTotal)

"""
leaves, which returns a list of the leaf labels of a tree

"""
def leaves(t):
    if if_leaf(t):
        return [label(t)]
    else:
        return [leaves(b) for b in branches(t)]

print(leaves(tree_fib3))

container=[]
def flat_arr(arr):
    for n in arr:
        if not isinstance(n,list):
            container.append(n)
        else:
            container.append(flat_arr(n))
    return container

test1 =[[1,[2]],[3,[4,[5,[6,[7]]]]]]

print(flat_arr(test1))

def flat_arr_f(arr):
    return sum([flat_arr_f(x) if isinstance(x,list) else x  for x in arr])

print(flat_arr_f(test1))

print(sum(test1,[]))

"""
input a tree and output another tree with all leaves add 1
"""
def tans_tree_with_one(t):
    if if_leaf(t):
        return tree(label(t)+1)
    else:
        return tree(label(t),[tans_tree_with_one(b) for b in branches(t)])

print("--------")
print(tree_fib3)
print(tans_tree_with_one(tree_fib3))

"""
input a tree and output another tree with all labels add 1
"""

def trans_tree_all_label(t):
    if if_leaf(t):
        return tree(label(t)+1)
    else:
        return tree(label(t)+1,[trans_tree_all_label(b) for b in branches(t)])


print("--------")
print(tree_fib3)
print(trans_tree_all_label(tree_fib3))

"""
print tree
"""
def print_tree(t):
    print(label(t))
    for b in branches(t):
        print_tree(b)

print_tree(fib_tree_f(3))


def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-2)+fib(n-1)
print("----")
print(fib(4))
print_tree(fib_tree_f(4))
print(fib_tree_f(3))

"""
print fib_tree in structure style:
[2,[1],[1,[0],[1]]

"""
def print_tree_str(t):
    if if_leaf(t):
        print('leaf',label(t))
    else:
        print(str(label(t))+"\n")
        for b in branches(t):
            print_tree_str(b)

# print_tree_str(fib_tree_f(3))

def print_tree_str_f(t,left):
    if if_leaf(t):
        if left ==1:  # left
            print("/")
            print('leaf',label(t))
        elif left ==2:
            print("\\")
            print('leaf', label(t))
    else:
        if left ==0:    # root
            print(str(label(t)) + "\n")
        elif left ==1:  # left
            print("/")
            print(str(label(t)))
        elif left ==2:   # right
            print("\\")
            print(str(label(t)))

        print_tree_str_f(branches(t)[0],1)

        print_tree_str_f(branches(t)[1],2)


# print_tree_str_f(fib_tree_f(3),0)

"""
print structure :
by line , each line operate three part tree(label(),[left,right]) => [1,[left],[right]]
"""

def print_tree_s(t):
    if if_leaf(t):
        print(label(t))
    else:
        p1,left,right= label(t),branches(t)[0],branches(t)[1]
        p2,p3 = label(left),label(right)
        if len(left)>1:
            left =branches(left)
        else:
            left=[]

        if len(right)>1:
            right =branches(right)
        else:
            right =[]
        print(p1,p2,p3)
        if len(left)>0:
            print_tree_s(left)
        if len(right)>0:
            print_tree_s(right)



# print_tree_s(fib_tree_f(3))

def print_next_line(p1,p2,p3):
    if p1== -1:
        print(p2,p3)
    else:
        print(p1)
        print(str("/"+str(p2)),str("\\"+str(p3)))

def print_tree_s_line(t):
    if if_leaf(t):
        print(label(t))
    else:
        p1,left,right = label(t),branches(t)[0],branches(t)[1]
        p2,p3 = label(left),label(right)
        if p1 == -1:
            p1=''
        print_next_line(p1,p2,p3)
        l_l,l_r,r_l,r_r=[],[],[],[]
        if len(left)>1:
            l_l,l_r = branches(left)[0],branches(left)[1]
        if len(right)>1:
            r_l, r_r = branches(right)[0], branches(right)[1]
        print_tree_s_line(-1,[list(l_l+l_r) ,list(r_l+r_r)])


# print_tree_s_line(fib_tree_f(4))


print("++++")

print_tree(fib_tree_f(3))


def print_tree_simple(t):
    print(label(t))
    for b in branches(t):
        print_tree_simple(b)
print("------")
print_tree_simple(fib_tree_f(3))

def print_tree_simple_s(t,indent=0):
    print(" " * indent + str(label(t)))
    for b in branches(t):
        print_tree_simple_s(b,indent+1)

print("-----")
print_tree_simple_s(fib_tree_f(10))

