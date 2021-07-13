def count(s,value):
    """ count the number of times which value appear in the s sequence
    >>> count([1,2,2,3],2)
    2
    >>> count([1,2,2,[2,2],3],2)
    4
    """
    total,index =0,0
    while index <= len(s)-1:
        if s[index] == value:
            total +=1
            index +=1
        else:
            index+=1
    return total

# assert count([1,2,2,3],2) == 2


def count_r(s,value):
    total,index =0,0
    while index <= len(s)-1:
        if isinstance(s[index],int):
            if s[index] == value:
                total,index = total+1,index+1
            else:
                index +=1
        elif isinstance(s[index],list):
            return total+ count_r(s[index],value)
    return total

assert count_r([1,2,2,[2,2,[2,3,[2,10]]],3],2) == 6

print(count_r([1,2,[3,2,[4,2,[5,2,[6,2]]]]],2))