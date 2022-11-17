"""
Email slicer is just a simple tool that will take multiple email adress as an input and 
slice it to produce the username and domain associated with it. The email must be divided 
into two strings bu using '@' symbol as seprator.
"""
# Code -->
entry = int(input("Enter the total number of entry's you want to make"))
lst = []
user = 1
def data():
    email_id = input("Enter your E-mail id -->")
    lst.append(email_id)
for i in range(entry):
    data()
for j in lst:
    d_info = j.split("@")
    print("\nUser {}".format(user))
    print("Usermame: {} ; Domain name: {}".format(d_info[0],d_info[1]))    
    user+=1