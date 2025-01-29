def fibo(n):
    x = [0, 1]
    a = 0
    b = 1
    for i in range(2, n):
        x.append(a+b)
        c = a + b
        a = b
        b = c
    return x

n = int(input("Enter number of Fibonacci you want: "))
print (fibo(n))