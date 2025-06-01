def input_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    return a, b, c

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
if __name__ == "__main__":
    a, b, c = input_numbers()
    print("The maximum of the three numbers is:", max_of_three(a, b, c))
