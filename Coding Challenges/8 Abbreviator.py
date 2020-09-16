# Abbreviator

def abbreviator(string):
    if len(string) < 5:
        return string
    else:
        return string[:4] + "."

string = input("Enter the input string: ")

print(abbreviator(string))