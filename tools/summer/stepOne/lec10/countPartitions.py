def count_part(n,m):
    if n==0:
        return 1
    elif n<0:
        return 0
    elif m==0:
        return 0
    with_m = count_part(n-m,m)
    without_m= count_part(n,m-1)
    return with_m+ without_m

# print(count_part(6,4))

c=[]
pp=[]


def part_p(n,m,p,left):
    if n==0:
        c.append(m)
        print(c)
        c.clear()
        c.append(pp[0])
        return 1
    elif n<0 or m==0:
        return 0
    elif n>0 and left:
        if len(pp)==0:
            pp.append(m)
        elif n>6-pp[0]:
            c.clear()
            pp.clear()
            pp.append(p)
        c.append(m)

    return part_p(n-m,m,m,True), part_p(n,m-1,m-1,False)




part_p(6,4,4,False)



