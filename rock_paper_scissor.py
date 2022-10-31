# Play a game of Stone,paper,scissor with your computer.

import random as r

def score(a,b):
    print("------------------------------------------")
    print("RESULT--> Best of Three")
    print("------------------------------------------")
    print("Your score is {} and computer score is {}".format(score_u,score_c))

    if score_c > score_u:
        print("Computer wins")
    elif score_u > score_c:
        print("You win")
    else:
        print("Draw")

flag = "Y"
while flag =="Y" or flag == "y":
    score_u = 0
    score_c = 0
    print("***********************")
    print("Best of Three")
    print("***********************")

    for i in range(3):
        ele = r.randint(0,2)
        lst = ["rock","paper","scissor"]
        inp = input("ROCK---PAPER---SCISSOR") 
        user = inp.lower()
        comp = lst[ele]
        print("Your input is {} and comp input is {}".format(user,comp))
        if user == comp:
            print("Draw")
        elif user[0] == "r":
            if comp[0] == "p":
                print("Computer wins")
                score_c+=1
            elif comp[0] == "s":
                print("You win")
                score_u+=1
        elif user[0] == "p":
            if comp[0] == "r":
                print("You win")
                score_u+=1
            elif comp[0] == "s":
                print("Computer wins")
                score_c+=1
        elif user[0] == "s":
            if comp[0] == "r":
                print("Computer wins")
                score_c+=1
            elif comp[0] == "p":
                print("You win")
                score_u+=1
        else:
            print("Enter correct input")

    score(score_c,score_u)
    flag = input("Enter Y to continue the game or enter N to leave the game")

print("-----------------------------------------")
print("Thank you for playing the game")
print("-----------------------------------------")