import random

def guess():
    a = 0
    b = 100
    i = 0
    while True:
        i += 1
        n = random.randint(a, b)
        r = input("Is " + str(n) + " your number?(Yes/Low/Higher)")
        if r[0].lower() == "y":
            print("I got it after", i, "attempt(s)")
            break
        elif r[0].lower() == "l":
            b = n-1
        elif r[0].lower() == "h":
            a = n + 1
        if a>b or b<a:
            print("IMPOSSIBLE")
            break

if __name__ == "__main__":
    guess()
    