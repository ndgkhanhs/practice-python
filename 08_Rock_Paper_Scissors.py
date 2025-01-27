import random

lists = ["rock", "paper", "scissors"]
cmd = input("Enter 'start' to play: ")
while (cmd != "start"):
    print("---WRONG COMMAND---")
    break
while (cmd == "start"):
    computer = random.choice(lists)
    player = input("Enter rock, paper or scissors: ") 
    if (player not in lists):
        print("---INVALID PLAY---")
        break
    if (player == computer):
        print("Computer choice: " + str(computer))
        print("---DRAW---")
    elif (player == 'rock' and computer == 'scissors') or \
       (player == 'scissors' and computer == 'paper') or \
       (player == 'paper' and computer == 'rock'):
        print("Computer choice: " + str(computer))
        print("---WIN---")
    else:
        print("Computer choice: " + str(computer))
        print("---LOSE---")
    cmd = input("Enter 'quit' to end game or 'start' to restart: ")
    if (cmd == "quit"):
        print("---Goodbye!---")
        break