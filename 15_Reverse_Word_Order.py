def revers(a):
    b = a.split()
    c = []
    for i in b:
        c.insert(0, i)
    return c

a = input("Enter a sentence: ")
print (revers(a))