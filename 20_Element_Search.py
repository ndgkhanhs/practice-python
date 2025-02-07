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
    start = 0
    end = len(b) - 1

    while start <= end:
        middle = (start + end) // 2
        if a < b[middle]:
            end = middle - 1
        else:
            start = middle + 1
    
    b.insert(start, a)
    return b

if __name__ == "__main__":
    b = list(map(int, input("Enter a list: ").split()))
    a = int(input("Enter a number to put in list: "))
    print(binarySearch(a, b))


    