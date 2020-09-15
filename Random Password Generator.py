#basic random password generator
print("***  Random Password Generator  ***".center(100, " "))

import random
length = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
pass1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pass2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pass2u = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
pass3 = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "."]
l = random.choice(length)
password = str()

while(True):
    if len(password) < l:
        p1 = random.choice(pass1)
        p2 = random.choice(pass2)
        p3 = random.choice(pass3)
        p2u = random.choice(pass2u)
        pu = str(p2u).upper()
        password += p1 + p2 + p3 + pu


    else:
        print(f"Password: \t [ {password[:l]} ] \t of Length '{l}' units")
        break
