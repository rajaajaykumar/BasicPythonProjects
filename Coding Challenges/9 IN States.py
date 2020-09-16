# Indian States
#import states from INstates

from INstates import states

def lookup_states(abbreviation):
#    abbreviation = abbreviation.upper()
    if abbreviation in states:
        return states[abbreviation]
    else:
        return "Sorry! Abbreviation Not Found"

abbreviation = input("Search for Your State through its abbreviation in CAPITAL: ")

print(lookup_states(abbreviation))
