import os, random, sys, time
from font import Font
from player import Player

class TicTacToe:
    def __init__(self):
        self.game_over = None
        self.play_field = self.generate_play_field()

        self.PLAY_FIELD_MARKER = ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2')

    @staticmethod
    def title_banner() -> None:
        title = """
            ___________.__         ___________               ___________            
            \__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
              |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
              |    |   |  \  \___    |    |   / __ \\  \___     |    |(  <_> )  ___/ 
              |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                               \/                 \/     \/                      \/ 
        """
        print("\t\t{0}{1}{2}\n\n".format(Font.set_style("BLINK", "LIGHT_BLUE"), title, Font.end_style()))

    @staticmethod
    def generate_play_field():
        return [[' '] * 3 for i in range(3)]

    @staticmethod
    def clear() -> None:
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def draw_board(self) -> None:
        self.clear()
        self.title_banner()

        for i in range(3):
            for j in range(2):
                if self.play_field[i][j] == ' ':
                    index = self.play_field_marker.index("{0},{1}".format(i,j))
                    print(" {0}{1}{2} ".format(Font.set_style("BLINK", "DARK_GRAY"), index, Font.end_style()), end = '|')
                else:    
                    print(" {} ".format(self.play_field[i][j]), end = '|')
            
            if self.play_field[i][2] == ' ':
                index = self.play_field_marker.index("{0},2".format(i))
                print(" {0}{1}{2} ".format(Font.set_style("BLINK", "DARK_GRAY"), index, Font.end_style()))
            else:
                print(" {} ".format(self.play_field[i][2]))
            if i < 2:
                print("-" * 12)
        
        print("\n" * 2)

    def get_available_moves(self) -> list:
        available_moves = list()
        for i in range(3):
            for j in range(3):
                if self.play_field[i][j] == ' ':
                    index = self.play_field_marker.index("{0},{1}".format(i,j))
                    available_moves.append(index)
        
        return available_moves

    def current_status(self, player: Player):
        print("Current Turn: {0}\t\tMarker: {1}".format(player.name(), player.marker()))
        print("Available Moves: {}".format(self.get_available_moves()))

    def if_won(self, marker: str) -> bool:
        left_diag = ''
        right_diag = ''

        has_won = False

        # Transpose play_field
        transpose = [*zip(*self.play_field)]

        for index in range(3): 
            left_diag += self.play_field[index][index]
            right_diag += self.play_field[index][2 - index]

            # Check Horizontally
            row = ('').join(self.play_field[index])

            if row == marker * 3:
                has_won = True
        
            # Check Vertically
            column = ('').join(transpose[index])

            if column == marker * 3:
                has_won = True
        
        if (left_diag == marker * 3) or (right_diag == marker * 3):
            has_won = True

        return has_won 

    def if_draw(self) -> bool:
        game_draw = False

        if len(self.get_available_moves()) == 0 and not self.game_over:
            game_draw = True
        
        return game_draw

    def display_winner(self, player: Player) -> None:
        self.draw_board()

        print("""{0}
            _________                                     __           ._._._.
            \_   ___ \  ____   ____    ________________ _/  |_  ______ | | | |
            /    \  \/ /  _ \ /    \  / ___\_  __ \__  \\   __\/  ___/ | | | |
            \     \___(  <_> )   |  \/ /_/  >  | \// __ \|  |  \___ \   \|\|\|
             \______  /\____/|___|  /\___  /|__|  (____  /__| /____  >  ______
                    \/            \//_____/            \/          \/   \/\/\/ 
        {1}""".format(Font.set_style("BLINK", "LIGHT_GREEN"), Font.end_style()))
        print("{} won the game !!!".format(player.name()))

    def display_draw(self) -> None:
        self.draw_board()
        print("""{0}
             ________                        ________                       
            /  _____/_____    _____   ____   \______ \____________ __  _  __
           /   \  ___\__  \  /     \_/ __ \   |    |  \_  __ \__  \\ \/ \/ /
           \    \_\  \/ __ \|  Y Y  \  ___/   |    `   \  | \// __ \\     / 
            \______  (____  /__|_|  /\___  > /_______  /__|  (____  /\/\_/  
                    \/     \/      \/     \/          \/           \/            
        {1}""".format(Font.set_style("BLINK", "LIGHT_PURPLE"), Font.end_style()))

    def make_play(self, player: Player):
        while True:
            self.draw_board()
            self.current_status(player)
        
            player_move = input("Please make a play: ")

            if player_move.isdigit():
                if int(player_move) in self.get_available_moves():
                    board_index = self.play_field_marker[int(player_move)]
                    i,j = map(lambda x: int(x), board_index.split(','))

                    # Set the move
                    self.play_field[i][j] = player.marker()

                    # Check if player won
                    if self.if_won(player.marker()):
                        self.display_winner(player)
                        self.game_over = True
                    
                    if self.if_draw():
                        self.display_draw()
                        self.game_over = True
                    
                    # End player turn
                    player.switch_turn()
                
                    break
                else:
                    print("That move is not available.")
                    time.sleep(1)
            else:
                print("Not a valid move !!\nTry Again.")
                time.sleep(1)

    """def ai_move(self, player: Player):
        outcome_score = -1000
        best_move = (-1, -1)

        # Create a copy of the board to run Minimax
        temp_field = self.play_field

        # Traverse through the board to make a play and evaluate
        for i in range(3):
            for j in range(3):"""

    
    def ai_play(self):
        marker = self.marker_choice()
        first_move = input("Do you wish to go first ?? (yes/no): ")

        if first_move.upper() in ['YES', 'YE', 'Y']:
            if marker == 'X':
                player1 = Player('Player1', 'X', True)
                player2 = Player('Computer', 'O', False)
            else:
                player1 = Player('Player1', 'O', True)
                player2 = Player('Computer', 'X', False)
        else:
            if marker == 'X':
                player1 = Player('Computer', 'O', True)
                player2 = Player('Player2', 'X', False)
            else:
                player1 = Player('Computer', 'X', True)
                player2 = Player('Player2', 'O', False)

        self.game_over = False

        while not self.game_over:
            if player1.move():
                if player1.name() == 'Computer':
                    self.ai_move(player1)
                else:
                    self.make_play(player1)

                player2.switch_turn()
            else:
                if player2.name() == 'Computer':
                    self.ai_move(player2)
                else:
                    self.make_play(player2)

                player1.switch_turn()
    
    def human_play(self):
        # 1. Get player 1 and player 2 markers
        # 2. Player 1 is x
        # 3. Player 1 moves first

        player1 = Player('PlayerA', 'X', True)
        player2 = Player('PlayerB', 'O', False)

        self.game_over = False

        while not self.game_over:
            if player1.move():
                self.make_play(player1)
                player2.switch_turn()
            else:
                self.make_play(player2)
                player1.switch_turn()

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
