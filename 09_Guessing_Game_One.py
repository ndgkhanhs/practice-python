import random
x = random.randint(1, 9)
cmd = input("Enter start to begin: ")
while (cmd == "start"):
    y = int(input("Enter a guess from 1 to 9: "))
    if (y == x):
        print("Correct number!!!")
        break
    elif (y < x):
        print("Bigger than that!")
    elif (y > x):
        print("Lower than that!")
    z = input("Enter 'exit' to end game: ")
    if (z == "exit"):
        print("The correct number is: " + str(x))
        break
    