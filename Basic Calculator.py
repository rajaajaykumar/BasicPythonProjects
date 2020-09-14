print("***  Basic Calculator  ***".center(100))
print("Enter 1st Number, then Select Operator from following, and then enter 2nd number")
print("Operators \t Functions")
print("\t+ \t\t for Addition")
print("\t- \t\t for Subtraction")
print("\t* \t\t for Multiplication")
print("\t/ \t\t for Division")
print("\t** \t\t for Power")
print("--> Press \"e\" to Exit  <--".center(100, " "))

while(True):
    key = input("Press Any Key except \"e\" to Continue: ")
    if key != "e":
        num1 = float(input("Enter the 1st number: "))
        operator = input("Select Operator: ")
        num2 = float(input("Enter the 2nd number: "))
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1-num2)
        elif operator == "*":
            print(num1*num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "**":
            print(num1**num2)
        else:
            print("Error! Unexpected Operator Input.")
    else:
        print("Thank you for using our Calculator!")

