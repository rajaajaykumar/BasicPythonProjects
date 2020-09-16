# Number of Things

def how_many(n, obj):
    if n == 1:
        return "There is " + str(n) + " " + obj + "."
    else:
        return "There are " + str(n) + " " + obj + "s."
n = int(input("Enter the Number of items/objects: "))
obj = input("Enter the item/object name: ")

print(how_many(n, obj))
