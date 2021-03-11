# 18117 = 7+1+1+8+1 =18
# 18117%10 =7 18117 //10 =1811

# this way is just use recursive method to resolve my iterator idea process.
# like translate the figure it out process to code
def sum_digit(n):
    def help_f(total,i):
        if i > 0:
            mid = i // 10
            dig = i % 10
            return help_f(total+dig,mid)
        else:
            return total
    return help_f(0,n)

assert sum_digit(18117) == 18

# real recursive philosophy : begin with the space of the issue resolve,
#
def sum_digit2(n):
    if n<10:  # this is the exit of recursive and the a part of space of resolve
        return n
    else:
        all_but_last,last = n//10, n % 10
        return sum_digit2(all_but_last)+last

# sum_digit2(18117)

# 4!= 4* 3*2*1

def fact(n):
    total=1
    index=n
    while index>=1:
        total,index= index*total,index-1
    return total

assert fact(4) ==24

def fact_r(n):
    if n==1:
        return 1
    else:
        return fact_r(n-1)*n

assert fact_r(4) ==24

# Mutual Recursion
# even or odd number,

def is_even(n):
    if n==0:
        return True
    elif is_odd(n-1):
        return True
    else:
        return False


def is_odd(n):
    if n==0:
        return False
    if is_even(n-1):
        return True
    else:
        return False


assert is_even(24) == True

# 0 is even and 1 is odd , which are the exit and basic base,
# use - to  the base, and the step is 1
# There are only two possible ,even or odd .
def is_even_all(n):
    if n==0:
        return True
    else:
        if (n-1)==0:
            return False
        else:
            return is_even_all((n-1)-1)

# Printing in Recursive Functions
def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

cascade(12345)

def alice(n):
    if n==1:
        print("alice Win")
        return True
    else:
        return bob(n-1)

def bob(n):
    if (n % 2 == 0 and n ==2) or n==1:
        print("bob Win")
        return True
    else:
        if n%2 ==0:
            return alice(n-2)
        else:
            return alice(n-1)

# n and let gamer 1 start
def game(n,gamer1):
    gamer1(n)


print(game(20,alice))

# Tree Recursion

# 0,1 (0+1),(1+1),(1+2),(2+3),(3+5)
# 0 1   1     2     3     5     8
#
def fib(n):
    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

assert fib(6)==8

def fib_num(n):
    i,total =2,0
    all_num= [0,1]
    if n==0:
        all_num.append(0)
        print (0)
    elif n==1:
        all_num.append(0)
        print (1)
    else:
        while i<=n:
            all_num.append(all_num[i-2]+all_num[i-1])
            i=i+1
        print(all_num)

# fib_num(5)

# Partitions
# 1 =1 2 =1+1 3= 2+1 = 1+1+1 ; 4=,3+1 = 2+1 ,1+1+1
# 6 = 2 + 4
# 6 = 1 + 1 + 4
# 6 = 3 + 3
# 6 = 1 + 2 + 3
# 6 = 1 + 1 + 1 + 3
# 6 = 2 + 2 + 2
# 6 = 1 + 1 + 2 + 2
# 6 = 1 + 1 + 1 + 1 + 2
# 6 = 1 + 1 + 1 + 1 + 1 + 1

# 1 easy: get all possible count


def parti(total,up_to,container):
    if (total == up_to == 1) or (total == up_to):
        container=container+1
    else:
        if( up_to > 1):
            i = 1
            while i <= up_to:
                total_n, i = total - i, i + 1
                if i > total_n:
                    i = total_n
                parti(total_n, i, container)
        else:
            if total-1>=1:
                parti(total-1,up_to,container)


    return container

# print(parti(2,1,0))
# assert parti(6,4) ==9
# (6,4) = (6-4,4) + (6,4-1)
#   n,m  =  n-m,m  +  n,m-1    把问题域 缩小了一步，且只是一步。 m 步长为1收缩，-> n 可以被m 步长为1 收缩，
#  m-1 -> m  给出边界条件，收敛指向的边界。convergence  m==0 对计数的贡献为 0
#  n-m -> n  n==0
# 递归的关键点在于 有效的找出以最简单，最有效的 相同的收缩逻辑，

#

def count_partitions(n,m):
    print(n,m)
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    else:
        with_m = count_partitions(n-m,m)
        without_m = count_partitions(n,m-1)
        return with_m+without_m

count_partitions(3,3)














