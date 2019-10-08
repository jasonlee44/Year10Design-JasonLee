import random
guess = False
tries = 0
answer = random.randint(1,100)
while guess == False:
    num = int(input("Guess a number between 1 and 100: "))
    if num == answer:
        print("You guessed it!")
        guess == True
    elif num > answer:
        print("Too high")
    else:
        print("Too low")
