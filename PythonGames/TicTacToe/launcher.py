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

            print("\t1.{0[1]:15}\n\t2.{0[2]:15}\n\t3.{0[3]:15}\n\n".format(choices))
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
                player2 = EasyComputer('Computer(Hard)', player2_marker, not(player1_first_move))

        print(player1)
        print(player2)

        # Generate Game
        # tic_tac_toe = TicTacToe()


if __name__ == "__main__":
    play = Launcher()
    play.launch_game()