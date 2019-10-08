'''
import random
guess = False
tries = 0
answer = random.randint(1,100)
while guess == False:
    num = int(input("Guess a number between 1 and 100: "))
    if num == answer:
        print(f"You guess it in {tries}")
        guess = True
    elif num > answer:
        tries += 1
        print("Too high")
    else:
        tries += 1
        print("Too low")
'''
import random
guess = False
tries = 0
answer = random.randint(1,100)
while guess == False:
    num = int(input("Guess a number between 1 and 100: "))
    if num == answer:
        print(f"You guess it in {tries} tries")
        guess = True
    elif num > answer:
        tries += 1
        print("Too high")
    else:
        tries += 1
        print("Too low")
