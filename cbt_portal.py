# @author: Paras Upadhyay
# Dated - November 2021

'''#----Functions are here---#'''

#entry_type() function asks for input for either registration or login
def entry_type():
        global choice
        global entry_granted
        choice= input("Register for a new account or Login if registered earlier\nType 'login' for login, or\nType 'register' for making a new account\n")
        choice=choice.lower()
        if choice == "login" or choice == "register":
                entry_granted = 1
             
#entry() function takes login or registration details for getting access to the program      
def entry():
        global name
        global password
        if choice == "login":
                print("\n---login---")
                print("*****\nPlease enter your username in lowercase only\n*****")
                name = input("Enter your Username : ")
                password = input("Enter your Password ,IF FORGOT PASSWORD press ENTER key:- ")
                if password=='':
                    print("\n------------------------------")
                    forgot_password()                 # Generates your password if forgotten password
                    print("\n------------------------------")
                    print('\nLogin again')
                    entry()
                else:
                    login(name,password)
#redirects you to the login() function
        else:
                print("\n---Register---\nEnter your details to make a new account")
                print("\n*****Please enter your username in lowercase only\n*****")
                name = input("Enter your username : ")
                password = input("Generate your password : ")
                register(name,password)             #redirects you to the register() function


#login() function checks if the details entered match with any of the registered details from the file 'Datafile'
def login(name,password):
        global success_granted
        global no_check
        global username_check
        success_granted = 0
        file = open("Datafile.txt",'r')
        for i in file:
                username_check,password_check,no_check = i.split(",")
                password_check = password_check.strip()
                no_check=no_check.strip()
                if username_check==name and password_check==password:
                        success_granted = 1
                        break
        file.close()      
               
#register() function creates a new registration in the 'Datafile' file
def register(name,password):
        global special_num
        global choice
        error = 0
        file = open("Datafile.txt",'r')
        for i in file:
                name_check,b,c = i.split(",")
                if name == name_check:
                        print("Username already exists, Enter another username or login")
                        print()
                        error = 1                        
        file.close()
       
        if error == 1:
                entry_type()
        else:                            
                file = open("Datafile.txt",'a')
                code_no()                        # Provides code no. to the user
                special_num = str(code_check())  # Checks entry of the code no.
                file.write(name+","+password+","+special_num)
                file.write('\n')
                file.close()
                print('\nPlease login again to start the quiz')
                choice = 'login'
                entry()

# Creates code_number to continue registration process used in future refrences
def code_no():  
    import random as r
    global random_number
    random_number = r.randint(100000,999999)
    print("\n******************************")
    print("Your secreat code number is--",random_number,"--please note down for future refrence\'s")
    print("******************************")

# Checks if user has entered correct or incorrect code number
def code_check():
    code=int(input("Enter your code number here to continue registration-"))
    if code == random_number:
        print("\nRegistration Successful")
        return code
    else:
        print('''You have entered incorrect code number,
              \nTaking you back to the starting page\nPlease once again make your registration ''')
        entry_type()
       
# Generates forgotten code_number
def forgot_code_no():
    a = 0
    global recovered_code
    file = open('Datafile.txt','r')    
    username = input("Enter your username")
    info=' '
    L_code=[]
    while info:
        info = file.readline()
        rdlst = info.split(',')
        if a==1:
            recovered_code=L_code[1]
            return recovered_code
            a=0
        else:
            L_code.clear()
        for no in rdlst:
            num=no.strip()
            if num ==username.lower():
                print("Code recovered")
                a=1
            else:
                L_code.append(num)
    file.close()
   
# Generates forgotten password
def forgot_password():
    code_number = input('Enter your code_number to get your password ,IF FORGOT CODE NO press ENTER key')
    global recovered_pass
    global password
    if code_number=='':
        print(forgot_code_no(),'is your recovered code number')
        forgot_password()
    else:
        fin= open('Datafile.txt','r')    
        info=' '
        L_pass=[]
        while info:
            info = fin.readline()
            rdlst = info.split(',')
            L_pass.clear()
            for no in rdlst:
                num=no.strip()
                if num == code_number:
                    recovered_pass=L_pass[1]
                    print('\nYour recovered password is ******',recovered_pass,'******')            
                else:
                    L_pass.append(num)
        fin.close()
       

#quiz() funtion conducts the quiz and takes user's answers. It later checks the answers and gives a total.
def quiz():
        global total
        global list_ans
        Responses = []
        print('---------------------------------------------')
        print('''\nPython is an interpreted high-level general-purpose programming language.\n
"It's design philosophy emphasizes code readibility with its use of significant
indentation. It's language constructs as well as its object-oriented approach,
aim to help programmers write clear,logical code for small as well as large
scale projects".\n
"This quiz will assess your basic knowledge about python and python programes"\n
----Let's get started with the quiz----''')
       
        print('''\n**Instructions regarding the quiz:-**\n
1) The quiz contains 12 questions and each question carries 2 marks.
2) All the questions are compulsory\n
ALL THE BEST\n''')
        print('--------------------------------------------')
        print()
        total = 0
        quiz_file= open("Quizfile.txt",'r')
        begin=input("Press Enter key to start the quiz\n")
        if begin=='':
            for line in quiz_file:
                if line != "\n":
                    print(line, end="")
                else:
                    ans = input("Enter you answer as (a,b,c,d): ")
                    Responses.append(ans)
                    print()
        else:
            print("xxxxxx WARNING Wrong key pressed xxxxxxxx")
            quiz()
        quiz_file.close()
        list_ans = ['c','c','a','d','b','a','a','c','b','b','a','c']
        for i in range(12):
                if Responses[i] == list_ans[i]:
                        total += 2
        return total


#total_saver() function saves the score in a file along with the name of the user
def total_saver():
        score = str(total)
        success = 0
        index = 0
        file = open("Recordfile.txt", 'r')
        for i in file:
                index += 1
                name_check,pass_check = i.split(",")
                pass_check = pass_check.strip()
                if name_check==name:
                        success = 1
                        break
       
        if success == 0:
                file = open("Recordfile.txt", 'w')
                file.write(name+","+score+'\n')
       
        else:
                file = open("Recordfile.txt", "r")
                info = file.readlines()
                info[index-1] = name+","+score+"\n"

                file = open("Recordfile.txt", "w")
                file.writelines(info)
                file.close()


#quiz_result() shows various result as per user's input
def quiz_result():
        answerkey = ['1->c\n','2->c\n','3->a\n','4->d\n','5->b\n','6->a\n','7->a\n','8->c\n','9->b\n','10->b\n','11->a\n','12->c\n']
        condition = input("Emter your code_no to get your score, or\nType 'Key' for answers, or\nType 'Leave' to quit the quiz\n")
        if  condition == no_check:
                file = open("Recordfile.txt",'r')
                for i in file:
                        display_name , display_score = i.split(",")
                        display_score = display_score.strip()
                        print("NAME:-",display_name.upper()+"  "+"SCORE:-",display_score)
                print()
                quiz_result()
        elif condition == "Key" or condition== 'key':
                ans1 = open("Answerfile.txt",'w')
                ans1.writelines(answerkey)
                ans1.close()
                ans2=open("Answerfile.txt",'r')
                content=ans2.read()
                print("Anwer key for the quiz is shown below:-\n ",content)
                ans2.close()
                quiz_result()
        elif condition == "Leave" or condition=='leave':
                print('\nTHANK YOU  for attempting the quiz\nHave a good day!')
        else:
                print("Invalid input")
                quiz_result()
                       

#---------Program starts here-------------
print('###########################################################\n')              
print("""Hello dear I welcome you to the trivia quiz where you will face some of the basic python programming problems##---
      \n***Be ready to face them***\n""")
print('############################################################')
start_re=input('Press Enter key to begin registration or login process for the quiz')

entry_granted = 0
success_granted = 0
entry_type()                              
while 1:
        while 1:
                if entry_granted == 1:
                        entry()
                        break
                else:
                        print("Please enter a valid command")
                        entry_type()

        if success_granted == 1:        #if the user is logged in successfully, he/she can take the quiz
                print("\nHello", username_check.upper(), "! You are logged in successfully")
   

                print("\nWARNING Your previous score will be overwritten if you take the quiz again")
                inp_ = input("Press enter to continue to the quiz")
                quiz()
                break
        else:
                print("Incorrect username or password") #if the initial input is invalid it asks for the input again
                print()
                entry_type()

total_saver()                                                           #score is saved after the quiz is taken
print("\nYou have completed the quiz\n")

quiz_result()