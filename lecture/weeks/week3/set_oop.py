s={2,3,4,5,6,7,90}
assert 3 in s
assert len(s)==7
assert s.union({10,20}) == {2,3,4,5,6,7,90,10,20}
assert s.intersection({30,90}) =={90}

# Use Link implement the set
class Link:
    empty=()
    def __init__(self,first,rest=empty):
        assert isinstance(rest,Link) or rest is Link.empty
        self.first = first
        self.rest= rest

    def __getitem__(self, i):
        if i==0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        if self.rest is Link.empty:
            return 1
        else:
            return 1+len(self.rest)

def link_expressions_2(s):
    if s.rest is Link.empty:
        rest= ''
    else:
        rest = ' ,' + link_expressions_2(s.rest)
    return 'Link({0}{1})'.format(str(s.first),str(rest))

Link.__repr__ = link_expressions_2

def map_link_(f,s):
    if s is Link.empty:
        return Link.empty
    elif s.rest is Link.empty:
        return Link(f(s.first))
    else:
        return Link(f(s.first),map_link_(f,s.rest))


def extent_link(s, t):
    # print('s:',s,'t:',t)
    if s is Link.empty:
        return t
    else:
        return Link(s.first, extent_link(s.rest, t))

def filter_link_(f,s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link_(f,s.rest)  # name is the important key to abstraction
        if f(s.first):
            return Link(s.first,filtered)
        else:
            return filtered

# Set use linked implements  unordered -style
def empty(s):
    return s is Link.empty

def set_contains(s,v):
    if s.first == v:
        return True
    elif s.first != v and s.rest == Link.empty:
        return False
    else:
        return set_contains(s.rest,v)

def adjoin_set(s,v):
    if set_contains(s,v):
        return s
    else:
        return Link(v,s)

s= Link(1,Link(3,Link(5,Link(4))))

print(set_contains(s,3))
print(set_contains(s,10))
s_new= adjoin_set(s,7)
print(s_new)


def union_set(set1,set2):
    """ Return a set containing all elements common to set1 and set2."""
    set1_all_not_in_set2 = filter_link_(lambda x: not set_contains(set2,x),set1)
    return extent_link(set1_all_not_in_set2,set2)

set1 = Link(1,Link(2,Link(3,Link(4))))
set2 = Link(10,Link(11,Link(2,Link(49))))

union_demo_1 = union_set(set1,set2)
print(union_demo_1)

# (1,2,4) intersect (1,89,90) =(1)
def intersect_set(set1,set2):
    return filter_link_(lambda x:set_contains(set2,x),set1)

intersect_demo_1 = intersect_set(set1,set2)
print(intersect_demo_1)

# if the set is ordered then we can do this:

def set_contians_(s,v):
    if empty(s) or s.first >v:
        return False
    elif s.first == v:
        return True
    else:
        return set_contians_(s.rest,v)

def intersect_set_(set1,set2):
    if empty(set1) or empty(set2):
        return Link.empty
    else:
        e1,e2 = set1.first,set2.first
        if e1 == e2:
            return Link(e1,intersect_set_(set1.rest,set2.rest))
        elif e1>e2:
            return intersect_set_(set1,set2.rest)
        elif e2>e1:
            return intersect_set_(set1.rest,set2)

set11 = Link(1,Link(2,Link(3,Link(20))))
set22 = Link(10,Link(11,Link(20,Link(49))))

intersect_set_demo_1 = intersect_set_(set11,set22)

print(intersect_set_demo_1)

# if the set is present by tree and in binary search trees

class Tree:
    def __init__(self,root,left,right):
        pass

    def __repr__(self):
        rest=''
        if self.branches:
            rest= ', '+ repr(self.branches)
        return 'Tree({0}{1})'.format(str(self.label),str(rest))

    def is_leaf(self):
        return not self.branches
# we can think carefully the process which is recursive
def set_contains_binary_tree(s,v):
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry >v:
        return set_contains_binary_tree(s.left,v)
    elif s.enty <v:
        return set_contains_binary_tree(s.right,v)

# we can feel the beautiful
def adjoin_set_binary_tree(s,v):
    if s is None:
        return Tree(v)
    elif s.entry == v:
        return s
    elif s.entry < v:
        return Tree(s.entry,s.left,adjoin_set_binary_tree(s.right,v))
    elif s.entry > v:
        return Tree(s.entry,adjoin_set_binary_tree(s.left,v),s.right)

print(type(set))


