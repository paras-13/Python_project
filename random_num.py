"""
In tis project you have to enter a range(A,B) and system will randomly pick any number from your given range
and check the status of that given number.

Properties to be checked are:
1. Is that numbe is odd or even 
2. Is that number is positive or negative number
3. Is that number is prime number or composite number.
"""

from random import randint as r

# Range for the program
num1 = int(input("Enter from where you want to start your range"))
num2 = int(input("Enter at where you want to end your range"))

r_num = r(num1,num2)
print()
print(r_num,"is the random number generated by the system")

def odd_even(num):
    if num%2 == 0:
        res = "is an Even number"
        return res
    else:
        res = "is a Odd number"
        return res

def pos_neg(num):
    if num>=0:
        res = "is a Positive number"
        return res
    else:
        res="is a Negative number"
        return res
def prime_num(num):
    if num>1:
        for i in range(2,num+1):
            if num%i == 0:
                res = "is a Composite number"
        else:
            res="is a Prime number"
            return res
    else:
        res = "is neither even nor odd number"
        return res
print("----------------------------------------------------------------------------------")
print("To check whether the random number generated is odd or even enter --> 1")
print()
print("To check whether the random number generated is positive or negative enter --> 2")
print()
print("To check whether the random number generated is prime or composite number enter--> 3")
print()
print("To end the program enter --> exit")
print("------------------------------------------------------------------------------------")

key = "Y"
while key == "Y" or key == "y":
    choice = input("Enter your choice as 1,2,3 or exit")
    if choice == '1':
        print(r_num,odd_even(r_num))
    elif choice == '2':
        print(r_num,pos_neg(r_num))
    elif choice == '3':
        print(r_num,prime_num(r_num))
    elif choice.lower() == "exit":
        key = "N"
    else:
        print("Choice should be 1, 2 or 3. You entered incorrect number")

print("Thank you!","Program ends",sep="\n")



    
    
    
    