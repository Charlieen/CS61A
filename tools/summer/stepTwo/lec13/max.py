temp = max(range(5))

print(temp)

assert max(range(10), key=lambda x:7-(x-4)*(x-2)) ==3

assert (lambda x:x+2)(2) ==4

assert bool(4) == True

assert all([x<5 for x in range(5)]) == True

assert all([0]) == False

