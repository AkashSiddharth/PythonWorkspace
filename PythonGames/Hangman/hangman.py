import json
import random
import os
import time

class Player:
    def __init__(self, name: str, lives: int):
        self.player = name
        self.player_lives = lives
        self.player_guesses = []

    def player_name(self) -> str:
        return self.player
 
    def lost_life(self):
        self.player_lives -= 1

    def fetch_player_lives(self) -> int:
        return self.player_lives
    
    def add_to_guess_stack(self, guessed_letter):
        self.player_guesses.append(guessed_letter)
    
    def fetch_guesses(self) -> list:
        return self.player_guesses


class HangMan:
    def __init__(self):
        self.category = None
        self.word = None
        self.play_field = None
        self.won = None
        self.replay = True

        self.played_words = []

        self.hangman_ascii = ['''
            +---+
            O   |
           /|\  |
           / \  |
               ===''', '''
            +---+
            O   |
           /|\  |
           /    |
               ===''', '''
            +---+
            O   |
           /|\  |
                |
               ===''', '''
            +---+
            O   |
           /|   |
                |
               ===''', '''
            +---+
            O   |
            |   |
                |
               ===''', '''
            +---+
            O   |
                |
                |
               ===''', '''
            +---+
                |
                |
                |
               ===''','''
                  
                 
                 
                 
                  ''']

        self.launch()

    def clear(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def is_won(self):
        if ''.join(self.play_field) == self.word:
            self.won = True
    
    def render_play(self, player: Player):
        # Wipe the playscreen
        self.clear()

        print("PLAYER: {0}\t\t\t\tPLAYER LIVES: {1}\n".format(player.player_name(), player.fetch_player_lives()))
        print("\t\t\t{}".format(self.hangman_ascii[player.fetch_player_lives()]))
        print("\n\nCATEGORY: {}\n".format(self.category.upper()))

        print('\t\t\t', end=' ')
        for field in self.play_field:
            print(field, end=' ')
        print("\n\nGUESSES: {}".format(player.fetch_guesses()))
    
    def load_word(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'HangMan.json'), 'r') as in_f:
        ## For Debugger
        # with open('D:\WorkSpaces\PythonWorkSpace\PythonGames\HangMan.json', 'r') as in_f:
            data = json.load(in_f)

        self.category = list(data)[random.randint(0, len(data.keys()) - 1)]
        self.word = data[self.category][random.randint(0, len(data[self.category]) - 1)]
        self.play_field = ['__'] * len(self.word)
    
    def ask_player(self, player: Player):
        while player.fetch_player_lives() > 0 and not self.won:
            self.render_play(player)
            letter = input("Make a guess: ")
            if letter not in player.fetch_guesses():
                if letter in self.word:
                    indices = [i for i, x in enumerate(self.word) if x == letter]
                    for index in indices:
                        self.play_field[index] = letter
                else:
                    print("Letter not present in the word, Try again")
                    time.sleep(1)
                    player.lost_life()
                
                player.add_to_guess_stack(letter)
            else:
                print("You have already tried this letter !!")
                time.sleep(2)
            
            self.is_won()
        
        if player.fetch_player_lives() == 0:
            self.clear()
            print('''\n\n\n\t\t\tHANG MAN
                    \tYOU FAILED TO GUESS "{0}"\n\n\n'''.format(self.word))
    
        if self.won:
            self.clear()
            print('''\n\n\n\t\t\tCONGRATULATIONS {0}
                    \tYOU GUESSED "{1}" CORRECTLY !!!\n\n\n'''.format(player.player_name(), self.word)) 
    
    def reset_play(self):
        self.won = False

    def launch(self):
        player_name = input("Please enter you the player's name: ").upper()

        while self.replay:
            self.won = False

            player_lives = len("HANGMAN")
            new_player = Player(player_name, player_lives)

            self.load_word()
            self. ask_player(new_player)

            retry = input("Do you wish to replay ??(yes/no) ")
        
            if retry.upper() in ['Y', 'YE', 'YES']:
                self.reset_play()

                # Delete the player object
                del new_player
            else:
                self.replay = False

if __name__ == "__main__":
    new_game = HangMan()
