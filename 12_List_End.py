import random

def r_list():
    a = random.sample(range(1,30), 15)
    return a

def short(a):
    print (str(a[0]) + " - " + str(a[-1]))
    return

a = r_list()
print (a)
short(a)
