import os, random, sys, time

# TO-DO
# 1. Tie condition
# 2. AI Engine for move weight calculation
# 3. AI Play 

class Player:
    def __init__(self, name, marker, first_move):
        self.player_name = name
        self.player_marker = marker
        self.current_turn = first_move

    def name(self) -> str:
        return self.player_name
    
    def marker(self) -> str:
        return self.player_marker
    
    def move(self) -> bool:
        return self.current_turn
    
    def switch_turn(self) -> None:
        self.current_turn = not(self.current_turn)

class TicTacToe:
    def __init__(self):
        self.game_over = None
        self.play_field = [[' '] * 3 for i in range(3)]
        self.play_field_marker = ['0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2']

        self.launch_game()

    def clear(self) -> None:
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def draw_board(self) -> None:
        self.clear()
        print("\t\tTIC TAC TOE\n\n")

        for i in range(3):
            for j in range(2):
                print(" {} ".format(self.play_field[i][j]), end = '|')
            print(" {} ".format(self.play_field[i][2]))
            if i < 2:
                print("-" * 12)
        
        print("\n" * 2)
    
    def draw_menu(self) -> int: 
        choices = { 1 : '1 Player', 2: '2 Players' }

        print("\t\tTIC TAC TOE\n\n")
        print("\t{0[1]:15}\n\t{0[2]:15}\n\n".format(choices))

        choice = int(input("Select play mode (1/2): "))

        return choice
    
    def launch_game(self) -> None:
        while True:
            self.clear()

            match self.draw_menu():
                case 1:
                    self.ai_play()
                case 2:
                    self.human_play()
                case _:
                    print("\n\t\tNOT A VALID INPUT !!!")
                    time.sleep(1)
                    continue

            exit(0)
    
    def get_available_moves(self) -> list:
        available_moves = list()
        for i in range(3):
            for j in range(3):
                if self.play_field[i][j] == ' ':
                    index = self.play_field_marker.index("{0},{1}".format(i,j))
                    available_moves.append(index)
        
        ## --To-Do-- 
        # If the list is empty, Display Game Tied message

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

    def display_winner(self, player: Player) -> None:
        self.draw_board()

        print("""
                                         _       
                                        | |      
          ___ ___  _ __   __ _ _ __ __ _| |_ ___ 
         / __/ _ \| '_ \ / _` | '__/ _` | __/ __|
        | (_| (_) | | | | (_| | | | (_| | |_\__ \\
         \___\___/|_| |_|\__, |_|  \__,_|\__|___/
                          __/ |                  
                         |___/                           
        """)
        print("{} won the game !!!".format(player.name()))

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
                    
                    # End player turn
                    player.switch_turn()
                
                    break
                else:
                    print("That move is not available.")
                    time.sleep(1)
            else:
                print("Not a valid move !!\nTry Again.")
                time.sleep(1)

    def marker_choice(self) -> str:
        marker = ''
        while True:
            self.clear()
            print("\t\tTIC TAC TOE\n\n")
            
            marker = input("\n\tChoose your marker (X / O): ")
            match marker.upper():
                case 'X':
                    marker = 'X'
                    break
                case 'O':
                    marker = 'O'
                    break
                case _:
                    print("\n\t\tNOT A VALID INPUT !!!")
                    time.sleep(1)
                    continue
        
        return marker

    def ai_move(self, player: Player):
        pass
    
    def ai_play(self):
        marker = self.marker_choice()
        first_move = input("Do you wish to go first ?? (yes/no)")

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
                player2 = Player('Player1', 'O', False)

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
