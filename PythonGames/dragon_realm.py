'''
In this game, the player is in a land full of dragons. 
The dragons all live in caves with their large piles of collected treasure. 
Some dragons are friendly and share their treasure. 
Other dragons are hungry and eat anyone who enters their cave. 
The player approaches two caves, one with a friendly dragon and the other with a hungry dragon, 
but doesn’t know which dragon is in which cave. 
The player must choose between the two.
'''

import time
import random

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
            you see two caves. In one cave, the dragon is friendly
            and will share his treasure with you. The other dragon
            is greedy and hungry, and will eat you on sight.\n''')

def chooseCave():
    choice = int(input("Which cave will you go into? (1 or 2) => "))

    if choice in [1,2]:
        return choice
    else:
        print("There is no other cave.")
        exit(0)

def consequence():
    choice = chooseCave()
    friendlycave = random.randint(1,2)

    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)

    if choice == friendlycave:
        print("Offers you his treasure !!!")
    else:
        print("Gobbles you down in one bite!")
    
    print("Game Over")

def runner():
    playAgain = bool(True)

    while playAgain:
        displayIntro()
        consequence()

        replay = input("Do you wish to play again? (yes/no) => ")

        if replay.upper() not in ['YES', 'YE' 'Y']:
            playAgain = bool(False)

if __name__ == "__main__":
    runner()