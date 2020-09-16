# Gerund Slicing

def gerund_infinitive(string):
    if string[-3:].lower() == "ing":
        return f"To {string[:-3]}"
    else:
        return "That\'s not a gerund!"

string = input("Enter the input: ")

print(gerund_infinitive(string))
