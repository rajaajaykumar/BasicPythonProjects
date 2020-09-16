# Morse Code

from morse import morse_code
def morsify(string):
    morsified = ""
    for letter in string:
        morsified += morse_code[letter]
    return morsified

stringIn = input("Enter the string to Morsify: ")
string = stringIn.upper()

print(morsify(string))
