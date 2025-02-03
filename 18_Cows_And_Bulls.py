import random

def sep(x):
    a = x//1000
    b = x//100%10
    c = x%100//10
    d = x%10
    return [a, b, c, d]

x = random.randint(1000, 9999)
i = sep(x)

n = int(input("Enter number: "))
j = sep(n)

#def CaB(n, x):

print(x)

