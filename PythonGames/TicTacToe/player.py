import time
import random
import math

class Player():
    def __init__(self, name, marker, first_move):
        # Private Properties
        self._player_name = name
        self._player_marker = marker
        self._current_turn = first_move
    
    def __str__(self):
        value = """
            {0}___________
            Marker:       {1}
            Current Turn: {2}
        """.format(self.name, self.marker, self.current_turn)
        return value

    @property
    def name(self) -> str:
        return self._player_name
    
    @property
    def marker(self) -> str:
        return self._player_marker

    @property
    def current_turn(self) -> bool:
        return self._current_turn
    
    @current_turn.setter
    def current_turn(self, turn: bool) -> None:
        self._current_turn = turn
    
    def get_move(self):
        pass

class HumanPlayer(Player):
    def __init__(self, name, marker, first_move):
        super().__init__(name, marker, first_move)
    
    def get_move(self, available_moves: list):
        valid_move = False
        while not valid_move:
            player_move = input("Please make a play: ")

            if player_move.isdigit():
                # Check if the provided position is in available moves
                if int(player_move) in available_moves:
                    valid_move = True
                else:
                    print("That move is not available.")
                    time.sleep(1)
            else:
                print("Not a valid move !!\nTry Again.")
                time.sleep(1)
        
        return int(player_move)

class EasyComputer(Player):
    def __init__(self, name, marker, first_move):
        super().__init__(name, marker, first_move)
    
    def get_move(self, available_moves: list):
        return available_moves[random.choice(range(len(available_moves)))]


class AIComputer(Player):
    def __init__(self, name, marker, first_move):
        super().__init__(name, marker, first_move)
    
    def get_move(self, game_obj: object):
        available_moves = game_obj.get_available_moves()
        # if first move, select at random
        if len(available_moves) == 9:
            best_move = available_moves[random.choice(range(len(available_moves)))]
        else:
            best_move = self.minimax(game_obj, self.marker, True)['position']
        
        return best_move

    def minimax(self, game, player, isMax: bool) -> dict:
        opponent = 'O' if player == 'X' else 'X'

        # Check the previous move won the game
        if game.game_state['game_over']:
            return {'position': None, 
                    'score': 1 * (len(game.get_available_moves()) + 1) if isMax 
                                                                       else
                            -1 * (len(game.get_available_moves()) + 1)
                   }
        elif len(game.get_available_moves()) == 0: # No moves left
            return {'position': None, 'score': 0}

        # set field score
        # if the turn is the maximizer turn then score set to 
        # negative infinity to maximize, else set to infinity
        # to minimize for opponent
        best_score = {'position': None, 'score': -math.inf if isMax else math.inf}

        # iterate over the moves
        for move in game.get_available_moves():
            game.make_move(move, player)
            simulation_score = self.minimax(game, opponent, not isMax)

            # undo move
            game.undo_move(move)

            # unset flags
            game.game_state = (False, None)

            # set the current move as the best possible move
            simulation_score['position'] = move

            # set score
            if isMax: # Maximize
                if simulation_score['score'] > best_score['score']:
                    best_score = simulation_score
            else: # Minimize
                if simulation_score['score'] < best_score['score']:
                    best_score = simulation_score
        
        return best_score
