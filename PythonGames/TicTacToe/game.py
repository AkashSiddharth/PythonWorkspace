import os, random, sys, time
from support import Font, Banners, Utility
from player import Player

class TicTacToe:
    def __init__(self):
        self._game_state = {
            "game_over": False,
            "winner": None
        }

        self._play_field = self.generate_play_field()

        self.PLAY_FIELD_MARKER = ('0,0', '0,1', '0,2', '1,0', '1,1', '1,2', '2,0', '2,1', '2,2')

    @property
    def game_state(self):
        return self._game_state

    @property
    def play_field(self):
        return self._play_field
    
    @game_state.setter
    def game_state(self, values):
        flag, marker = values
        self._game_state['game_over'] = bool(flag)
        self._game_state['winner'] = marker

    @staticmethod
    def generate_play_field():
        # Generate a 2-D 3 X 3 array
        return [[' '] * 3 for i in range(3)]

    def draw_board(self) -> None:
        for i in range(3):
            for j in range(2):
                if self.play_field[i][j] == ' ':
                    index = self.PLAY_FIELD_MARKER.index("{0},{1}".format(i,j))
                    print(" {0}{1}{2} ".format(Font.set_style("BLINK", "DARK_GRAY"), index, Font.end_style()), end = '|')
                else:    
                    print(" {} ".format(self.play_field[i][j]), end = '|')
            
            if self.play_field[i][2] == ' ':
                index = self.PLAY_FIELD_MARKER.index("{0},2".format(i))
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
                    index = self.PLAY_FIELD_MARKER.index("{0},{1}".format(i,j))
                    available_moves.append(index)
        
        return available_moves

    def winner(self, marker: str) -> bool:
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

    def undo_move(self, position: int) -> None:
        # Convert the player index into 2-D board index
        board_index = self.PLAY_FIELD_MARKER[position]
        i,j = map(lambda x: int(x), board_index.split(','))

        # clear the position
        self.play_field[i][j] = ' '

    def make_move(self, position: int, marker: str) -> None:
        # Convert the player index into 2-D board index
        board_index = self.PLAY_FIELD_MARKER[position]
        i,j = map(lambda x: int(x), board_index.split(','))

        # Set the marker at the position
        self.play_field[i][j] = marker

        # Check the game state for a win/loss/draw
        if self.winner(marker):
            self.game_state = (True, marker)

if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
