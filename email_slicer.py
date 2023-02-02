"""
Email slicer is just a simple tool that will take multiple email adress as an input and 
slice it to produce the username and domain associated with it. The email must be divided 
into two strings bu using '@' symbol as seprator.
"""
# Code -->
entry = int(input("Enter the total number of entry's you want to make : "))
lst = []
user = 1
print(f"You are making {entry} entry's\nEnter mail id's for each:--")
def data(i):
    email_id = input(f"Enter mail id of {i+1}st client -->")
    lst.append(email_id)
for i in range(entry):
    data(i)
for j in lst:
    d_info = j.split("@")
    print("\nUser {}".format(user))
    print("Usermame: {} ; Domain name: {}".format(d_info[0],d_info[1]))    
    user+=1
print("Thank you for using this email slicer")