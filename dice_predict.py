"""
Design a project where as an input student will give astaticc number(between 1 and 6) and then roll the dice which randomly generate some value between 1 to 6.
The winning situation arrives when the given static/fixed number exactly same to the numbercame after rolling the dice.

User can play the game as many times he wants until user want to exit, and  whenever wining situation occur some scores must be given to the user, and
these scores goes on adding if user play this game number times.
"""
# Code -z

from random import randint as r
from time import sleep as s
print()
print("Dice game")
print("-- In this game you have to predict a number that will appear on the dice. --")
print("-- With each win you will gain 2 points")
print()

def roll_dice():
    r_num = r(1,6)
    return r_num
key = "Y"
won,loose = 0,0
while key.upper() == "Y":
    predict = int(input("Ok let's get started \nPredict a number that will appear on the dice -->"))
    print("\nYour predicted number -->",predict)
    inp = input("Press Enter key to roll the dice")
    if inp == "":
        print("Rolling.......")
        s(4)
        dice_num = roll_dice()
        print("\nNumber came up in the dice is -->",dice_num)
        if dice_num == predict:
            print("\nYou win")
            won += 1
        else:
            print("\nYou loose")
            loose += 1
        key = input("If you want to play again enter Y otherwise enter N")
    else:
        print("You pressed wrong key. Play again........\n")
score = won*2
total = won+loose
print("\nYou played {} games. Out of which you won :-{} amd you loose :-{} \nYour total score is {} points".format(total,won,loose,score))
print("Thank you for playing this game.")