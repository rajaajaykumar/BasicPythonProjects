import random

lst = ["Rock", "Paper", "Scissor"]
computer = random.choice(lst)
name = input("Type Your Name: ")

choice = input(f"{name}'s choice: ")
choice = choice.lower()

if choice == "r" or choice == "rock":
    choice = "Rock"
elif choice == "p" or choice == "paper":
    choice = "Paper"
elif choice == "s" or choice == "scissor":
    choice = "Scissor"

print()
print(f"{name}: [\"{choice}\"] \t\t\t Computer: [\"{computer}\"]")
print()

if choice == "Rock":
    if computer == "Rock":
        print("It's a Tie!")
    elif computer == "Paper":
        print("You Lost.")
    elif computer == "Scissor":
        print("Hurray! You Won.")
elif choice == "Paper":
    if computer == "Paper":
        print("It's a Tie!")
    elif computer == "Scissor":
        print("You Lost.")
    elif computer == "Rock":
        print("Hurray! You Won.")
elif choice == "Scissor":
    if computer == "Scissor":
        print("It's a Tie!")
    elif computer == "Paper":
        print("You Lost.")
    elif computer == "Rock":
        print("Hurray! You Won.")
