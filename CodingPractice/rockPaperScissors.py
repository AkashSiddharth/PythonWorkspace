''' Problem: Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
             print out a message of congratulations to the winner, and ask if the players want to start a new game)
                Remember the rules:
                    Rock beats scissors
                    Scissors beats paper
                    Paper beats rock
'''

if __name__ == "__main__":
    rules = { "rock" : "scissors", 
              "scissors" : "paper",
              "paper" : "rock"
            }

    player1 = input("Rock -- Paper -- Scissors: ")
    player2 = input("Rock -- Paper -- Scissors: ")

    if (player1.lower() in rules.keys()) and (player2.lower() in rules.keys()):
        if player1.lower() == player2.lower():
            print("{0} vs {1}, Its a draw!!".format(player1, player2))
        elif rules[player1.lower()] == player2.lower():
            print("{0} vs {1}, Player 1 wins!!".format(player1, player2))
        else:
            print("{0} vs {1}, Player 2 wins!!".format(player1, player2))
    else:
        print("Invalid Input")
