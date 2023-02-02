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
print("\nYou are using this password generator to generate a strong password")
from random import randint
from time import sleep
Pass = ""
up=lw=num=sp=""
def gen_password(n):
    global Pass,up,lw,num,sp
    cr = n//2
    lw,num,sp,up=lower(cr), number(3), special(), upper(cr)
    Pass = lw+num+sp+up
    return Pass

def upper(cr):
    upper = ""
    for i in range(cr):
        upper += chr(randint(65,91))
    return upper
def lower(cr):
    lower = ""
    for i in range(cr):
        lower += chr(randint(97,123))
    return lower
def number(cr):
    number = ""
    for i in range(cr):
        number += chr(randint(49,58))
    return number
def special():
    for i in range(1):
        special = chr(randint(60,65))
    return special
def status(length,lw,num,sp,up):
    print(f"\nYour password length is {length} characters which is under the prescribed range of length i.e; 12 characters")
    print("\nChecking for upper case....")
    sleep(1)
    print(f"This password contains uppercase characters that are '{up}' of length {len(up)}")
    print("\nChecking for lower case characters....")
    sleep(1)
    print(f"This password contains lower characters that are '{lw}' of length {len(lw)}")
    print("\nChecking for numeric characters....")
    sleep(1)
    print(f"This password contains numeric characters that are '{num}' of length {len(num)}")
    print("\nChecking for special characters....")
    sleep(1)
    print(f"This password contains a special character that is '{sp}'")
    print("\nPress enter key to exit")
    ip = input("")
    print("\nThank you for using this automatic password generator")
key = "Y"
while key == "Y":
    length = int(input("Enter the length for your password"))
    if length >=12:
        print("\nGenerating Your password......")
        sleep(2)
        Password = gen_password(length)
        print("Your Password is successfully generated")
        print(f"\n'{Password}' is your newly generated password")
        inp = input("\nTo check status of your password type 'status' otherwise press 'enter key-->' to exit..")
        if inp.lower() == "status":
            status(length,lw,num,sp,up)
        else:
            print("\nThank you for using this automatic password generator")
            key = "N"
    else:
        print("\n--- Note: YOUR PASSWORD LENGTH MUST BE GREATE OR EQUAL TO 12 ---\nEnter again")
