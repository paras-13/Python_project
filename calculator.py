# Program to make a calculator
# Information
print()
print("Welcome to the digital calculator")
print()
print("Enter 1 to perform addition")
print("Enter 2 to perform subtraction")
print("Enter 3 to perform multiplication")
print("Enter 4 to perform division")
print("Enter 5 to calculate exponent of a number")
print("Enter 6 to calculate under root of a number")
print("Enter exit to exit this calculator")
print()
print("---------------------------------------------------")

import math as m


def add(num1,num2):
    res=num1+num2
    return res
def sub(num1,num2):
    res = num1-num2
    return res
def prod(num1,num2):
    res= num1*num2
    return res
def div(num1,num2):
    res= num1/num2
    return res
def exp(num,pow):
    res = num**pow
    return res
def ur(num,pow):
    res = num**(1/pow)
    return res

key = "Y"
while key=="Y":
    choice  = input("Enter your choice")
    if choice == '1':
        print("Enter two numbers which you want ro add")
        n1,n2 = int(input("Enter first number")),int(input("Enter second number"))
        print("Sum of the given number is -->",add(n1,n2))
        print("-------------------------------------------------------")

    elif choice == '2':
        print("Enter two numbers which you want to subtract")
        n1,n2 = int(input("Enter first number")),int(input("Enter second number"))
        print("Difference of the given number is -->",sub(n1,n2))
        print("-------------------------------------------------------")

    elif choice == '3':
        print("Enter two numbers which you want to multiply")
        n1,n2 = int(input("Enter first number")),int(input("Enter second number"))
        print("Product of the given number is -->",prod(n1,n2))
        print("-------------------------------------------------------")

    elif choice == '4':
        print("Enter two numbers which you want to divide")
        n1,n2 = int(input("Enter first number")),int(input("Enter second number"))
        print("Division of the given number is -->",div(n1,n2))
        print("-------------------------------------------------------")
    
    elif choice == '5':
        print("Enter number whose exponent you want calculate")
        n1,n2 = int(input("Enter the number")),int(input("Enter the power to which you want to raise it"))
        print("Exponent of the given number is -->",exp(n1,n2))
        print("--------------------------------------------------------")
    elif choice == '6':
        print("Enter number whose under root you want to calculate")
        n1,n2 = int(input("Enter the number")),int(input("Enter the by which you want to find it's root"))
        print("Under root of the given number is -->",ur(n1,n2))
        print("--------------------------------------------------------")
    elif choice.lower() == "exit":
        key = "N"
    else:
        print("Enter a corrext choice,Your chouce should be 1,2,3,4 or exit")
print()

print("Thank you for using this calculator")