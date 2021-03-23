four = [1, [2, [3, [4, 'empty']]],[2],[4]]
# print(type(four))
# print(four.__len__())

#four = [1, [2, [3, [4, 'empty']]]]

empty='empty'

def is_link(s):
    return s==empty or (len(s)==2 and is_link(s[1]))

def link(first,rest):
    assert is_link(rest),"rest must be a linked list"
    return [first,rest]

def first(s):
    assert is_link(s),"first only applies to linked lists"
    assert s!=empty,"empty linked list has no first element"
    return s[0]

def rest(s):
    assert is_link(s)
    assert s!=empty
    return s[1]


l1= link(5,empty)
print(l1)
l2= link(4,l1)
l3= link(3,l2)
print(l3)

ll1 = link(1,link(2,link(3,link(4,empty))))
assert first(ll1) ==1
assert rest(ll1)==[2,[3,[4,'empty']]]

def len_link(s):
    length =0
    while s!= empty:
        s=rest(s)
        length = length +1
    return length

# ll1 [1,[2,[3,[4,'empty']]]]
def getitem_link(s,i):
    r, k = s, 0
    while i-1>0:
        r=rest(r)
        i=i-1
    return first(r)
# print(getitem_link(ll1,4))

def len_link_r(s,count=0):
    if s==empty:
        return count
    else:
        return len_link_r(rest(s),count+1)

print(len_link_r(ll1))

def getitem_link_r(s,i):
    if i-1==0:
        return first(s)
    else:
        return getitem_link_r(rest(s),i-1)


assert(getitem_link_r(ll1,2)) ==2

def extend_link(s,t):
    """ Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s==empty:
        return t
    else:
        return link(first(s),extend_link(rest(s),t))

test_s=[1,[2,'empty']]
test_t =[10,[20,'empty']]

print(extend_link(test_s,test_t))
#assert extend_link(test_s,test_t)==[1,[2,'empty'],10,[20,'empty']]

def apply_to_all_link(f,s):
    assert is_link(s)
    if s== empty:
        return s
    else:
        return link(f(first(s)),apply_to_all_link(f,rest(s)))

# ll1 [1,[2,[3,[4,'empty']]]]
print(apply_to_all_link(lambda x:2*x,ll1))

def filter_to_all_link(f,s):
    assert is_link(s)
    if s==empty:
        return s
    else:
        fir = first(s)
        if f(fir):
            return link(fir,filter_to_all_link(f,rest(s)))
        else:
            return filter_to_all_link(f,rest(s))

print(filter_to_all_link(lambda x:x>2,ll1))

# ll1 [1,[2,[3,[4,'empty']]]]
def join_link(s,separator):
    assert is_link(s)
    if s == empty:
        return separator
    else:
        fir = first(s)
        separator = str(fir)+ separator
        return join_link(rest(s),separator)



def join_link_2(s,separator):
    def join_link_help(s,separator,acc):
        assert is_link(s)
        if s == empty:
            return acc
        else:
            fir = first(s)
            if acc == '':
                acc=str(fir)+separator
            else:
                acc =acc  +str(fir)+separator
            return join_link_help(rest(s),separator,acc)
    return   join_link_help(s,separator,'')

print(join_link_2(ll1,','))


def parti(n,m):
    if n==0:
        return 1
    elif n<0 or m==0:
        return 0
    else:
        return parti(n-m,m)+parti(n,m-1)

# def parti_link(n,m):
#     def parti_link_help(n,m,l):
#         if n==0:
#             return l
#         elif n<0 or m==0:
#             return ['empty']
#         else:
#             return extend_link(parti_link_help(n-m,m,link(n-m)))
#     return parti_link_help(n,m,[0,'empty'])
#
# print(parti_link(6,4))

def branches(tree):
    if type(tree) == int:
        return False
    else:
        return tree[1:]

def is_tree(tree):
    if type(tree) !=list or len(tree)<1: # make sure all element(in tree) was in list
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def tree(root_label, branches_=[]):
    if len(branches_)==0:
        return [root_label]
    else:
        for branch in branches_:
            assert is_tree(branch), 'branches must be tree'
            return [root_label] + list(branches_)

def parti_tree(n,m):
    if n==0:
        return tree(True)
    elif m==0 or n<0:
        return tree(False)
    else:
        with_m, without_m = parti_tree(n-m,m), parti_tree(n,m-1)
        return tree(m,[with_m,without_m])


def parti_link(n,m):
    if n==0:
        return link(empty,empty)
    elif n<0 or m==0:
        return empty
    else:
        using_m =parti_link(n-m,m)
        with_m= apply_to_all_link(lambda s:link(m,s),using_m)
        without_m =parti_link(n,m-1)
        return extend_link(with_m, without_m)


# print(parti_link(6,4))
# print(parti_tree(3,3))

def print_parti(n,m):
    lists = parti_link(n,m)
    strings = apply_to_all_link(lambda s:join_link_2(s," + ") ,lists)
    print(join_link_2(strings,"\n"))

print_parti(6,4)


# Implementing Lists and Dictionaries

def mutable_link():
    """ Return a functional implementation of a mutable linked list."""
    contents =empty
    def dispatch(message,value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message =='getitem':
            return getitem_link(contents,value)
        elif message =='push_first':
            contents= link(value,contents)
        elif message =='pop_first':
            f= first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(", ")
    return dispatch

def to_mutable_link(source):
    """ Return a functional list with the same contents as source"""
    s = mutable_link()
    for element in reversed(source):
        s('push_first',element)
    return s

def dictionary():
    """ Return a functional implementation of a dictionary"""
    records=[]
    def getitem(key):
        matches = [r for r in records if r[0]==key]
        if len(matches)==1:
            key,value = matches[0]
            return value
    def setitem(key,value):
        nonlocal records
        non_matches = [ r for r in records if r[0]!=key]
        records = non_matches +[[key,value]]
    def dispatch(message,key=None,value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            return setitem(key,value)
    return dispatch

# By storing the balance in the dispatch dictionary rather than in the account frame directly,we
# avoid the need for nonlocal statement in deposit and withdraw
def account(initial_balance):
    # balance =0  # in account frame
    def deposit(amount):
       # nonlocal  balance
        dispatch['balance']+= amount
        return dispatch['balance']
    def withdraw(amount):
        if amount> dispatch['balance']:
            return 'Insufficient funds'
        else:
            dispatch['balance'] -= amount
            return dispatch['balance']
    dispatch={'deposite':deposit,'withdraw':withdraw,'balance': initial_balance}
    return dispatch

def withdraw(account,amount):
    return account['withdraw'](amount)
def deposit(account,amount):
    return account['deposite'](amount)
def check_balance(account):
    return account['balance']


a= account(20)
deposit(a,5)
withdraw(a,15)
assert check_balance(a) ==10

