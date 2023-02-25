"""
Create a multiplication table application where user will enter a sentinel value n and the
application will display the mathematical multiplication tables till given sentinel value n.
For example, if user enters n = 4 then application will display the multiplication tables of 2, 3,
and 4.
Constraint:
 Make use of oop concepts class methods and attributes
(Student is free to decide the input and output layout for this mini project)
"""
# using oops concept
class Tables:
    def __init__(self,n):
        self.num = n
    def table(self):
        for i in range(2,self.num+1):
            print(f"Printing table of {i}")
            for j in range(1,11):
                print(f"{i} x {j} = {i*j}")
            print("\n---------------------------\n")

def main():
    key = 'y'
    while key == 'y':
        stu1 = Tables(int(input("Enter a number upto which you want multiplication table")))
        stu1.table()
        key = input("Want to run again y/n")
main()