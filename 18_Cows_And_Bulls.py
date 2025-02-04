import random

def sep(x):
    a = x//1000
    b = x//100%10
    c = x%100//10
    d = x%10
    return [a, b, c, d]

def compare(x, n):
    cows, bulls = 0, 0

    for i in range(4):
        if x[i] == n[i]:
            cows += 1
        elif x[i] in n:
            bulls += 1
    
    return cows, bulls

def CaB():
    cows = 0
    bulls = 0
    x = random.randint(1000, 9999)
    a = sep(x)
    while True:
        n = int(input("Enter a number: "))
        nlen = str(n)
        if (len(nlen) != 4):
            print ("---INVALID INPUT---")
            continue
        b = sep(n)
        cows, bulls = compare(a,b)
        print (f"Number of cows: {cows}")
        print (f"Number of bulls: {bulls}")
        print (a)
        if cows == 4:
            print ("You completed the game!!!")
            break

if __name__ == "__main__":
    CaB()
    

