'''
Here’s what the Guess the Number program looks like to the player when it’s run. The player’s input is marked in bold.
    Hello! What is your name?
    Albert
    Well, Albert, I am thinking of a number between 1 and 20.
    Take a guess.
    10
    Your guess is too high.
    Take a guess.
    2
    Your guess is too low.
    Take a guess.
    4
    Good job, Albert! You guessed my number in 3 guesses!
'''

def runner():
  import random
  num_to_guess = random.randint(1,20)

  player = input("Hello! What is yout name? \n")

  print("Well, {}, I am thinking of a number between 1 and 20.".format(player))

  def ask_guess(prompt, guesses = 3):
    try:
      while True:
        guess = int(input(prompt))

        if guess > num_to_guess:
          print("Your guess is too high.")
        elif guess < num_to_guess:
          print("Your guess is too low.")
        else:
          print("Good job, {}! You guessed my number in 3 guesses!".format(player))
            
        guesses = guesses - 1

        if guesses == 0:
          print("{0}, You failed to guess my number({1}). GAME OVER!!!".format(player, num_to_guess))
          break
    except ValueError:
      print("Provided guess must be a number !!")

  ask_guess("Take a guess.")

if __name__ == "__main__":
  runner()