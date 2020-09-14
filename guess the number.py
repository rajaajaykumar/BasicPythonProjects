print("***  guess the number  ***".center(100, " "))
i = 9
print(f"Total Attemps: {i}")
print("Press \"h\" for Hint".center(100, " "))
print("\t Enter your guess value")

while(True):
    userInput = input()
    i -= 1
    if i != 0:
        if userInput == "h":
            print(f"It is {len(str(2020))} digit number")
        elif int(userInput) > 2020:
            print(f"No! Enter a \"Smaller\" value \t\t [Attempts Left: {i}]")
        elif int(userInput) < 2020:
            print(f"No! Enter a \"Greater\" value \t\t [Attempts Left: {i}]")
        elif int(userInput) == 2020:
            print("Eureka!:) You got it. It's Correct.")
            break
        else:
            print("Error :(")
    else:
        print(f"Sorry! You Lost. Try Again. \t\t [Attempts Left: {i}]")
        break
