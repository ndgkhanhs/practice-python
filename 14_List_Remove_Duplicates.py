def dup(a):
    #b = set(a)
    #c = list(b)
    #return c
    return list(set(a))

a = [1, 2, 3, 2, 4, 6, 3, 4]
print (dup(a))