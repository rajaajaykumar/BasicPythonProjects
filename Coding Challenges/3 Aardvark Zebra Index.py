# Aardvark Zebra Index
#If the input string starts with "a", it'll print aarkvard, else it'll print zebra

def aardvark(string):
    if string[0].lower() == "a":
        return "aardvark"
    else:
        return "zebra"

string = input("Enter the Input: ")

print(aardvark(string))
