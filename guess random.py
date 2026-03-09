import random

number = random.randrange(1,50)
solved = False
print("Guess a number")
while not solved:
    guess = int(input("enter number between 1 to 50:"))
    if guess>number:
        print("Greater number")
    elif guess<number:
        print("Lower number")
    elif guess==number:
        print("correct number")
    else:
        print("game over")
        solved = True