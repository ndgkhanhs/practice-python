number = int(input("Enter a number: "))
if (number%2==0):
    print("This number is even")
else:
    print("This number is odd")
if (number%4==0):
    print("This number is a multiple of 4")
num = int(input("Enter a number: "))
check = int(input("Enter a number to divide " + str(num) + ":"))
evenly = check/num
if (evenly==num):
    print(str(check) + " divides evenly into " + str(num))
if (evenly!=num):
    print(str(check) + " is not divides evenly into " + str(num))