#Basic way
"""
def compare(a, b):
    b.sort()
    for i in range(len(b)):
        if a < b[i]:
            continue
        else:
            b.append(a)
            b.sort()
            break
    return b

if __name__ == "__main__":
    b = list(map(int, input("Enter a list of number: ").split()))
    a = int(input("Enter a number to add to list: "))
    compare(a, b)
    print(b)
"""
#Use binary search
def binarySearch(a, b):
    b.sort()
    