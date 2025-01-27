import random

#a = [random.randint(1, 30) for _ in range(random.randint(5, 10))]
#b = [random.randint(1, 30) for _ in range(random.randint(5, 15))]
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
a.sort()
b.sort()
print(str(a) + "\n" + str(b))
c = [i for i in a if i in b]
print(c)
