print("***  Dice Roller  ***".center(100, " "))
print()
print("[Press \"q\" or \"quit\" to Quit the Rolling]")
print()

import random
dice = [1, 2, 3, 4, 5, 6]
while(True):
    key = input("Press any key to Roll: ")
    key = key.lower()
    if key == "q" or key == "quit":
        print("[Quit]")
        print("Thank You for Rolling the Dice!")
        break
    else:
        d = random.choice(dice)
        print(f"Dice Rolling... \t [You got \"{d}\" ]")
        print()
