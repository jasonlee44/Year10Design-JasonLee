import random

money = int(input("How much money do you want to bet: "))
x = ["Rock","Paper","Scissor"]

while money > 0:
    user = int(input("\nPlease choose (1: Rock, 2: Paper, 3: Scissor): ")) -1
    comp = int(random.randint(0,2))
    print(f"You: {x[user]}")
    print(f"Computer: {x[comp]}")
    if x[user] == x[comp]:
        print("*TIE!*")
    elif x[user] == "Rock" and x[comp] == "Paper":
        print("*You lose!*")
        money -= 5
    elif x[user] == "Paper" and x[comp] == "Scissor":
        print("*You lose!*")
        money -= 5
    elif x[user] == "Scissor" and x[comp] == "Rock":
        print("*You lose!*")
        money -= 5
    else:
        print("*You win!*")
        money = money + 5
    print(f"You have ${money}")

if money < 0:
    print("\nYou are now in debt. Have fun!")
    
else:
    print("\nYou have no more money. Incredible job!")