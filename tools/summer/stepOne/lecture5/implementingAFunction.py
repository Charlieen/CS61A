def remove(n,digit):
    """
    Return all digits of non-negative N that
    are not DIGIT, for some non-negative DIGIT less than 10.
    >>> remove(231,3)
    21
    >>> remove(243132,2)
    4313
    :param n:
    :param digit:
    :return:
    #1: for int number from right to left, get the last position useing %
    #2: for int number from right to left, get the new number without the last postion number using //
    #3: the condition of finishing the loop is less than 10
    """
    skiper,index ='', n
    while index>10:
        tail = index % 10
        if tail != digit:
            skiper = str(tail)+ skiper
            index = index // 10
        else:
            index = index //10
    if index != digit:
        skiper = str(index)+skiper
    return skiper

print(remove(2346383,3))


