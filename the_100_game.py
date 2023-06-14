# The 100 game --> creaed by the Reverand Charles Luwidge Dodgson
# Played between two players, both the players choose a number between 1-10 one by one and the one who reaches first as sum = 100 will win this game.
import random
import time
name = input("Enter your name :- ")
print(f"Good Luck! {name}")
sum = 0
ch = input("Enter 1 if you want to play first else 2")
if (ch == '1'):
    while sum <= 100:
        print("\nYour choice....")
        inp = int(input(">"))
        sum += inp
        print("SUM = ",sum)
        if (sum == 100):
            print("Congratulation! You win.")
            break
        cmp = random.randint(1,10)
        print("\nComputer choice...")
        time.sleep(1)
        print(">",cmp)
        sum += cmp
        print("SUM = ",sum)
        if (sum == 100):
            print("You loose computer wins.")
            break
        time.sleep(1)
elif (ch == '2'):
    while sum <= 100:
        cmp = random.randint(1,10)
        print("\nComputer choice...")
        time.sleep(1)
        print(">",cmp)
        sum += cmp
        print("SUM = ",sum)
        if (sum == 100):
            print("You loose computer wins.")
            break
        time.sleep(1)
        print("\nYour choice....")
        inp = int(input(">"))
        sum += inp
        print("SUM = ",sum)
        if (sum == 100):
            print(f"Congratulation! {name} You win.")
            break
else:
    print("Wrong selection try again...")
    

