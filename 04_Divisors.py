n = int(input("Enter a number: "))
a = []
for i in range(1,n):
    if (n%i==0):
        a.append(i)
print(a)

