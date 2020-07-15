''' Problem: Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess
             the number, then tell them whether they guessed too low, too high, or exactly right.
             Extras:
                    -- Keep the game going until the user types “exit”
                    -- Keep track of how many guesses the user has taken, and when the game ends, 
                        print this out.
'''
import random
import sys

def validate():
    guess = input("Enter your guess: ")
    if guess.isdigit():
        return int(guess)
    else:
        if guess in ('EXIT', 'exit', 'Exit'):
            print("Thank you for playing")
            sys.exit()
        else:
            print("Invalid Input")

if __name__ == "__main__":
    num = random.randint(1,9)
    no_Of_Guesses = 0
    while True :
        p_guess = validate()
        no_Of_Guesses += 1
        gap = abs(num - p_guess)

        if num == p_guess:
            print("Exactly Right!")
            print("It took you {0} guesses".format(no_Of_Guesses))
            sys.exit()
        elif num < p_guess:
            if gap >= 10:
                print("Too High")
            else:
                print("High")
        else:
            if gap >= 10:
                print("Too Low")
            else:
                print("Low")
        
    