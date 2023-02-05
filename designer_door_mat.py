# Hackerrank problem
# Program to print designer carpet.
# Here row is an odd number and col is third multiple of row
# For :eg--> 9 27, 11 33, 7 21

row,col = int(input('Enter row length')),int(input("Enter column length"))         # Defining variables
ch = ".|."
wel = "WELCOME"

def upper(row,col,ch):                  # Function to print upper layer design
    for i in range(row//2):
        exp = ch*(2*i+1)
        print(exp.center(col,"-"))

def middle(row,col,wel):                # Function to print middle level design
    print(wel.center(col,"-"))

def bottom(row,col,ch):                 # Function to print lower level design
    for i in range(row//2):
        exp = ch*((row-2)-2*i)
        print(exp.center(col,"-"))

if __name__ == "__main__":              # Calling functions
    upper(row,col,ch)
    middle(row,col,wel)
    bottom(row,col,ch)