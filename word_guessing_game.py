# Words guessing game
"""
In this game, there is a list of words present, out of which interpreter will choose 1 random word. 
The user first has to input their names and then, will be asked to guess any alphabet. 
If the random word contains that alphabet, it will be shown as the output(with correct placement) 
else the program will ask you to guess another alphabet. The user will be given 15 turns(which can be changed accordingly) 
to guess the complete word.

"""
import random
print("\n\t\t........Welcome to word guessing game.......\n")
name = input("Enter your name :- ")
print(f"Good Luck! {name}")
words = ["Algorithm", "Binary", "Compiler", "Encryption", "Firewall", "Graphics", "Kernel", "Cyber", "Networking", "Protocol", "Software", "Virtualization"]
print(".........Interpreter has selected a random word now your turn is to guess that word........")
print("\nHINT --> Number of underscores shows the length of word...Use only lowercase charater\n")
word = random.choice(words)
guesses = ""
turns = 15
while turns > 0:
    failed = 0
    for ch in word:
        if ch.lower() in guesses:
            print(ch, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    
    if failed == 0:
        print("\n\nYou win...")
        print("The word is :- ",word)
        break
    print()
    guess = input("\nGuess a character :- ")
    print()
    guesses += guess
    if guess not in word.lower():
        turns -= 1
        print("\n### Wrong ###")
        print(f"Now you have {turns} more guesses left")
        
        if turns ==0 :
            print("You loose")
    else:
        print(":)")
