import random

a = random.randint(1, 9)
b = random.randint(0, 9)
c = random.randint(0, 9)
d = random.randint(0, 9)

x = a*1000 + b*100 + c*10 + d 

print (x)

n = int(input("Number: "))

one = n//1000
two = n//100%10
three = n%100//10
four = n%10

print (one, two, three, four)