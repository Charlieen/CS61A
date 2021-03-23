from datetime import date
now= date(2021,3,13)

print(now)
print(now-date(1979,11,10))

assert now.year == 2021
# https://docs.python.org/3/library/datetime.html
print(now.strftime('%A,%B %d'))

print(type('1234'))
assert type('1234') == str
'1234'.isnumeric()

'Abc,dE nIRO'.swapcase()



chinese=['coin','string','nian']
suits=chinese

suits.append('chagangzi')
suits.extend([1,2,3])

print(chinese)

nest = list(suits)
print(nest)
nest[0]=suits
print(nest)

suits.extend([10,20])
print(nest)

suits_1=['heart', 'diamond', 'spade', 'club']
nest_1 =list(suits_1)

nest_1[0]=suits_1
suits_1.insert(2,'Joker')
joke= nest_1[0].pop(2)

# Two objects are identical if they are equal in their current value, and any change to one will always be reflected in the other
assert suits_1 is nest_1[0]  # this is Identity
assert suits is not ['heart', 'diamond', 'spade', 'club']
assert suits_1 == ['heart', 'diamond', 'spade', 'club'] # this is equality

from unicodedata import lookup
print([lookup('WHITE '+s.upper()+' SUIT') for s in suits_1])

# Tuples

print( type((1,2+3)))
print((True,[1,2],33,({1:100}),{'a':1000}))

tuples_1 =()
tuples_2 =(10,)
assert len(tuples_1) ==0
assert len(tuples_2) ==1

code =("up", "up", "down", "down") + ("left","right")* 2
assert len(code)== 8
assert code.count("down") == code.count("left")
assert code.index("left")==4
assert code.index("right")==5

tuples_3=(10,20,[3,4])
tuples_3[2].pop()
assert tuples_3==(10,20,[3])
print(tuples_3)
# assert tuples_3.pop() ==(20,[3,4]) # 'tuple' object has no attribute 'pop'

# Dictionaries correspondence relationships keys and values are objects, by descriptive keys

numerals={'I':1,'V':5,'X':10}

print(numerals.keys())
keys_numerals = numerals.keys();
values_numerals= numerals.values()
items_numerals= numerals.items()

print(type(keys_numerals)) #<class 'dict_keys'>
print(type(values_numerals)) #<class 'dict_values'>
print(type(items_numerals)) #<class 'dict_items'>
# assert type(numerals.keys()) == list

dict_1 = dict([(3,4),(4,5)])
print(type(dict_1))

#
#dict_2=dict([(3,4),([1],900)]) #TypeError: unhashable type: 'list'
#print(type(dict_2))

dict_2_2_0= {(1,2):100}
print(dict_2_2_0)
dict_2_2_1= dict([((1,2),100),((2,3),500)])
print(dict_2_2_1)

dict_3= dict([(3,4),(3,100)]) # dict_3 :{3:100} overwrite the first key =3 value =4
print(type(dict_3))

print(dict_3)
print(numerals.get('I'))

dic_gen_1={x:x*x for x in range(1,5)}
list_gen_1 =[x*x for x in range(1,5)]

print(type(list_gen_1))
print(list_gen_1)

print(type(dic_gen_1))
print(dic_gen_1)

# nonlocal

# The balance associated with a particular withdraw function is shared among all calls to that function.
# In this way , each instance of withdraw maintains its own balance state,but that state is inaccessible to
# any other function in the program

# It changes over time based on its own history of withdraw requests.

def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount> balance:
            return 'Insufficient funds'
        balance = balance -amount
        return balance
    return withdraw

charlie_withdraw = make_withdraw(1000)
fiona_withdraw = make_withdraw(2000)
fiona_son_withdraw = fiona_withdraw

fiona_son_withdraw(80)
first_f_1= fiona_withdraw(10)
assert fiona_withdraw(90) == 1820

first_1= charlie_withdraw(100)

first_1= charlie_withdraw(500)

assert charlie_withdraw(100) == 300

# Propagating Constraints

# def connect():
#     pass
# def connector():
#     pass
# def multiplier():
#     pass
# def adder():
#     pass
# def constant():
#     pass

# assert celsius['set_val']('user',25) # Celsius =25 Fahrenheit =77.0
# assert fahrenheit['set_val']('user',212) #Contradiction detected: 77.0 vs 212 Celsius =100.0 Fahrenheit =212
#
# assert celsius['forget']('user') # Celsius is forgotten Fahrenheit is forgotten

from operator import add, sub


def inform_all_except(source, message, constraints):
    """Inform all constraints of the message,except source"""
    for c in constraints:
        if c != source:
            c[message]()


def connector(name=None):
    """A connector between constraint"""
    informant = None
    constraints = []

    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'forget', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)

    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector


def adder(a, b, c):
    """ The constraint that a+b =c"""
    return make_ternary_constraint(a, b, c, add, sub, sub)


def make_ternary_constraint(a, b, c, ab, ac, bc):
    """The constraint that ab(a,c)=c and ca(c,a)=b and cb(c,b)=a"""
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ac(a['val'], c['val']))
        elif bv and cv:
            c['set_val'](constraint, bc(b['val'], c['val']))

    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)

    constraint = {'new_val': new_value, 'forget_value': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint


from operator import mul, truediv


def multiplier(a, b, c):
    """ Return constrainst that a*b =c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)


def constant(connector, value):
    """The constraint that connector = value"""
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint


def converter(c,f):
    """ Connect c to f with constraints to convert from Celsius to Fahrenheit"""
    u,v,w,x,y = [connector() for _ in range(5)]
    multiplier(c,w,u)
    multiplier(v,x,u)
    adder(v,y,f)
    constant(w,9)
    constant(x,5)
    constant(y,32)



celsius= connector('Celsius')
fahrenheit= connector('Fahrenheit')
converter(celsius,fahrenheit)





