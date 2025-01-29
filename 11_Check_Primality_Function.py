def prime(n):
    count = 0
    for i in range(2,n):
        if (n%i==0):
            count = count + 1
    if (count == 0):
        print ("This is a prime number")
    else: print ("This is not a primary number")

prime(int(input("Enter a number: ")))
