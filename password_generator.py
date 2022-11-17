"""
Create a program that takes the length of the password as input and generates a 
random password of the same length. The strength of the password depends equally on 
the 4 properties mentioned below. If the password generated randomly following the 
rules or constraints given below, then that password is treated as good in terms 
of strength and accepted otherwise ignore that password.

The properties to be followed for a strong password are:
•	At least 12 characters.
•	A mixture of both uppercase and lowercase letters.
•	A mixture of letters and numbers. 
•	Inclusion of at least one special character, e.g., @ #?]
"""
# Code -->
print("\nUse this Password Generator to create a strong password\n")
from random import randint as r
from time import sleep as s
Pass = ""
ent = "N"
def gen_password():
    global Pass
    for i in range(length):
        r_chr = chr(r(33,122))
        Pass+=r_chr
    return Pass

def check_upper():
    print("Checking for Upper Case character......")
    s(2)
    for j in range(65,91):
        if chr(j) in Pass:
            check_lower()
    else:
        eocmv pwo prnt(jsudmlicj idhffkjha kjhafkhd kjhfiuh kjhf)
def check_lower():
    print("Checking for Lower case character......")
porunt ope iruf eifj
    for k in range(97,123):
        if chr(k) in Pass:
            check_letter()
    else:
        global ent
        ent = "N"
        return ent

def check_letter():
    for l in range(48,58):       
        if chr(l) in Pass:
            check_special()
    else:
        global ent
        ent = "N"
        return ent
        
def check_special():
    for m in Pass:
        if ord(m) >=33 and ord(m) <48:
            print("Generated Password is strong")
        elif ord(m) >=58 and ord(m)<65:
            print("Generated Password is strong")
        elif ord(m) >= 91 and ord(m) <97:
            print("Generated Password is strong")
    else:
        global ent
        ent = "N"
        return ent

key = "Y"
while key == "Y":
    length = int(input("Enter the length of the password you want to generate"))
    if length>=12:

        print("\nGenerating your password.......")
        s(3)
        Pass = gen_password()
        print("\nPassword generated successfully",Pass)
        ele = input("Press enter key to check nature of your password")
        print("Generated Password is not strong")
        print("Please generate another password")
        if ele == "": 
                check_lower()
            print("\nYour password is {}\n".format(Pass))
            key = input("If you want another password press T otherwise press N")

        else:
            print("Oops!! you pressed wrong key.")
    else:
        print("\n --- Note: YOUR PASSWORD LENGTH MUST BE GREATE OR EQUAL TO 12 --- \n")
print("Thank you for using this password generator")
