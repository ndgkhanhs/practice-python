a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if (i<5):
        print(i)


b = []
for i in a:
    if (i<5):
        b.append(i)
print(b)

print([i for i in a if i<5])

n = int(input("Enter a number to compare: "))
for i in a:
    if (i<n):
        print (i)