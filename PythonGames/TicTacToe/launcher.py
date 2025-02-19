from player import HumanPlayer, EasyComputer, AIComputer
from game import TicTacToe
from support import Font, Banners, Utility
import os, time

class Launcher:
    def main_menu(self) -> int:
        choices = { 1: 'vs Human', 2: 'vs Computer (Easy)', 3: 'vs Computer (Hard)' }

        while True:
            Utility.clear()
            Banners.title_banner()

            print("\t1. {0[1]:15}\n\t2. {0[2]:15}\n\t3. {0[3]:15}\n\n".format(choices))
            choice = int(input("Select play mode (1-3): "))

            if choice in range(1,4):
                break
            else:
                print("\n\t\tNOT A VALID INPUT !!!")
                time.sleep(1)
                continue

        return choice
    
    def marker_choice(self) -> str:
        marker = ''
        while True:
            Utility.clear()
            Banners.title_banner()
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

    def first_move(self):
        Utility.clear()
        Banners.title_banner()

        move = input("Do you wish to go first ?? (yes/no): ")
        if move.upper() in ['YES', 'YE', 'Y']:
            return True
        else:
            return False

    def current_status(self, game, player) -> None:
        print("Current Turn: {0}\nMarker: {1}".format(player.name, player.marker))
        print("Available Moves: {}".format(game.get_available_moves()))

    def display_winner(self, game, player) -> None:
        Utility.clear()
        Banners.title_banner()
        game.draw_board()
        Banners.winner_banner()
        print("{} won the game !!!".format(player))

    def display_draw(self, game) -> None:
        Utility.clear()
        Banners.title_banner()
        game.draw_board()
        Banners.game_draw_banner()

    def redraw_play_field(self, game, player) -> None:
        Utility.clear()
        Banners.title_banner()
        game.draw_board()
        self.current_status(game, player)

    def launch_game(self) -> None:
        game_choice = self.main_menu()
        player1_marker = self.marker_choice()
        player2_marker = "O" if player1_marker.upper() == 'X' else 'X'
        player1_first_move = self.first_move()

        # Create Players
        match game_choice:
            case 1:
                player1 = HumanPlayer('Player1', player1_marker, player1_first_move)
                player2 = HumanPlayer('Player2', player2_marker, not(player1_first_move))
            case 2:
                player1 = HumanPlayer('Player1', player1_marker, player1_first_move)
                player2 = EasyComputer('Computer(Easy)', player2_marker, not(player1_first_move))
            case 3:
                player1 = HumanPlayer('Player1', player1_marker, player1_first_move)
                player2 = AIComputer('Computer(Hard)', player2_marker, not(player1_first_move))

        # Generate Game
        tic_tac_toe = TicTacToe()

        while len(available_positions := tic_tac_toe.get_available_moves()) > 0:
            if player1.current_turn:
                self.redraw_play_field(tic_tac_toe, player1)
                # print(player1)
                postion = player1.get_move(available_positions)
                tic_tac_toe.make_move(postion, player1.marker)
            else:
                self.redraw_play_field(tic_tac_toe, player2)
                # print(player2)
                postion = player2.get_move(tic_tac_toe) if game_choice == 3 else player2.get_move(available_positions)
                tic_tac_toe.make_move(postion, player2.marker)
            
            game_state = tic_tac_toe.game_state

            if game_state['game_over']: # If game over then display winner
                winner = player1.name if game_state['winner'] == player1.marker else player2.name
                self.display_winner(tic_tac_toe, winner)
                break
            else: # If game not over, switch turns and continue
                for obj in [player1, player2]:
                    obj.current_turn = not obj.current_turn      
        else: # If no available moves and no winners then its a draw
            self.display_draw(tic_tac_toe)

if __name__ == "__main__":
    play = Launcher()
    play.launch_game()