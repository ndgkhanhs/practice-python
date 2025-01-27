import random

a = [random.randint(1, 100) for _ in range(random.randint(1, 10))]
print ("This is list a: " + str(a))
print ("Even value in list a: " + str([i for i in a if i%2==0]))