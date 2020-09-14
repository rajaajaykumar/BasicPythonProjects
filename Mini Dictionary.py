#Mini Dictionary

d = {"joy": "a feeling of great pleasure and happiness", "learn" : "gain or acquire knowledge of or skill in (something) by study, experience, or being taught", "knowledge" : "facts, information, skills, awareness or familiarity gained by experience", "intelligence" : "ability to acquire and apply knowledge and skills", "engineer" : "a person who designs, builds, or maintains machines, or structures", "software" : "the programs and other operating information used by a computer", "computer": "an electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program"}
userInput = input("Enter the Word to Search for: ")

if userInput.lower() in d:
    print(f"Meaning of \"{userInput}\" is:")
    print(f"\"{d[userInput]}\"")
else:
    print("Sorry! Word Not Found")
    print(f"Click here to Search Online: https://www.dictionary.com/browse/{userInput}")
