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

def link_expressions(s):
    def help_(s,acc):
        if s.rest is Link.empty:
            return acc+s.first
        else:
            return help_(s.rest,acc+s.first)
    return help_(s,"")

Link.__repr__= link_expressions

# get head and tail , head = first, tail need to be recursive so just think about the rest
# after finished the rest,then  that mean: we have first and rest ,
# then use str format function to replace the params

#
def link_expressions_2(s):
    if s.rest is Link.empty:
        rest= ''
    else:
        rest = ' ,' + link_expressions_2(s.rest)
    return 'Link({0}{1})'.format(str(s.first),str(rest))

Link.__repr__ = link_expressions_2


link_demo_1 = Link('0',Link('1',Link('2',Link('3'))))

print(link_demo_1)

print(len(link_demo_1))

print(link_demo_1[2])
print(link_demo_1[3])

def extent_link(s,t):
    # print('s:',s,'t:',t)
    if s is Link.empty:
        return t
    else:
        return Link(s.first,extent_link(s.rest,t))

link_demo_2 = Link('a',Link('b',Link('c')))

ext_1_2 =extent_link(link_demo_1,link_demo_2)

print(ext_1_2)
print(len(ext_1_2))

def map_link(f,s):
    if s is Link.empty:
        pass
    else:
        f(s.first)
        return map_link(f,s.rest)

# print(type(link_demo_2))
# map_link(lambda x:print(x),link_demo_2)

def map_link_2(f,s):
    def help_(f,s,acc):
        if s is Link.empty:
            return acc
        else:
            return help_(f,s.rest,extent_link(acc,Link(f(s.first))))
    return help_(f,s.rest,Link(f(s.first)))

def map_link_(f,s):
    if s is Link.empty:
        return Link.empty
    elif s.rest is Link.empty:
        return Link(f(s.first))
    else:
        return Link(f(s.first),map_link_(f,s.rest))


# print(link_demo_2)
# map_demo =map_link_2(lambda x:'1'+x,link_demo_2)
# print(map_demo)
#
# map_demo_1 =map_link_(lambda x:'1'+x,link_demo_2)
# print('same:? ',map_demo_1)

def filter_link(f,s):
    def help_(f,s,acc):
        if s is Link.empty:
            return acc
        else:
            if f(s.first):
                return help_(f,s.rest,extent_link(acc,Link(s.first)))
            else:
                return help_(f,s.rest,extent_link(acc,Link.empty))
    return help_(f,s,Link.empty)


def filter_link_(f,s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link_(f,s.rest)  # name is the important key to abstraction
        if f(s.first):
            return Link(s.first,filtered)
        else:
            return filtered

# link_demo_3 = Link(1,Link(2,Link(3,Link(4))))
#
# print(link_demo_3)
# print(filter_link(lambda x:x<=2,link_demo_3))
# print(filter_link_(lambda x:x<=2,link_demo_3))


def join_link(s,operator):
    def help_(s,operator,acc):
        if s is Link.empty:
            return acc
        else:
            if acc == '':
                acc = str(s.first)
            else:
                acc= acc+operator+str(s.first)
            return help_(s.rest,operator,acc)
    return help_(s,operator,'')

# print(join_link(link_demo_3,'-'))

def join_link_(s,operator):
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + operator + join_link_(s.rest,operator)

# print(join_link_(link_demo_3,'--'))

def partitions(n,m):
    if n==0:
        return Link(Link.empty)
    elif n<0 or m==0:
        return Link.empty
    else:
        using_m = partitions(n-m,m)
        with_m = map_link_(lambda s:Link(m,s), using_m)
        without_m = partitions(n,m-1)
        return extent_link(with_m,without_m)

def print_partitions(n,m):
    lists = partitions(n,m)
    print(lists)
    strings = map_link_(lambda s:join_link_(s," + "),lists)
    print(join_link_(strings,"\n"))

print_partitions(3,2)

# begin list used python inner list implemented
empty=''
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

def apply_to_all_link(f,s):
    assert is_link(s)
    if s == empty:
        return s
    else:
        return link(f(first(s)),apply_to_all_link(f,rest(s)))

def extend_link(s,t):
    """ Return a list with the elements of s followed by those of t."""
    assert is_link(s) and is_link(t)
    if s==empty:
        return t
    else:
        return link(first(s),extend_link(rest(s),t))

    

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


# end