import random 

print("Welcome to the game of Head and Tails\n\t\t\t\tHead == 1\n\t\t\tTails == 2")


choose = str(input("Make a call for Head or tail ? :-"))

ran = random.randint(1,2)


if ran == 1:
    print(f"You have choosen {choose} and you got Head")
else:
    print(f"You have choosen {choose} and you got Tails")
