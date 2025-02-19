import random
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if (i in b and i not in c):
        c.append(i)
print (c)
"""

x = [random.randint(1, 100) for _ in range(random.randint(10, 20))]
y = [random.randint(1, 100) for _ in range(random.randint(10, 20))]
x.sort()
y.sort()
print ("X list number: " + str(x) + "\n" + "Y list number: " + str(y))
z = list(set([i for i in x if i in y]))
z.sort()
print (z)