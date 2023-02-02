# Project 5:

# The task is to create a script that generates a random number between a fixed range, and if the 
# user guesses the number right in three chances, then user wins otherwise user lose.

#  When a user guesses a number that is greater than a randomly selected number, the
# user receives the message “have one more try”. Your guess was too high.
#  If the user guesses a number smaller than a randomly selected number, the user gets an
# output of “have one more try “. Your guess was too small”
#  In addition, if the user guesses within a minimum number of attempts, they get a
# “Congrat’s” message and also get the winning scores.
#  If the user fails to guess the integer in the minimum number of guesses, he/she will
# receive a “Better Luck Next Time!
# (Student is free to decide the input and output layout for this mini project)
from random import randint
from time import sleep
print("\n--Are you ready to play a number guessing game with me---")
inp = input("Okay then press enter key to start this game")
def random_num(n1,n2):
    r = randint(n1,n2)
    return r

print("\n------INFORMATION--------")
print("NOTE : You will get only three chances to guess a number right\n")
print("Score will be generated the number of time you guessed it right in one or multiple games subsequently")
# Main Code-->
key = "y"
scr = 0
while key.lower() == "y":
    if inp == "":
        print("\n--Enter a range of numbers between which you want to guess this number--")
        print("\nNumbers should have a minimal difference of atleast 30")
        n1 = int(input("Enter starting range number --> "))
        n2 = int(input("Enter ending range number --> "))
        print("\nOkay you have given a range between which now I will generate a number")
        print("\n--Generating random number.....")
        r_num = random_num(n1,n2)
        sleep(2)
        print("\nNumber is successfully generated now it's your turn to guess it right")
        choice = 0
        for i in range(3):
            choice = int(input("Guess the number...."))
            if choice < r_num:
                print("Have one more try..Your guess was too low")
            elif choice > r_num:
                print("Have one more try...Your guess was too high")
            else:
                print("Congrat's..You guessed it correcly")
                scr += 1
                break
    if choice != r_num:
        print("Better luck next Time...")

    key = input("\nWant to play again y/n")
print(f"\nYou Quit this game\nThank you for playing it\nYour score is --> {scr}")



