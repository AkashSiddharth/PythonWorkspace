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
    def switch_turn(self) -> None:
        self.current_turn = not(self.current_turn)
    
    def get_move(self):
        pass

class HumanPlayer(Player):
    def __init__(self, name, marker, first_move):
        super().__init__(name, marker, first_move)

class EasyComputer(Player):
    def __init__(self, name, marker, first_move):
        super().__init__(name, marker, first_move)

class AIComputer(Player):
    def __init__(self, name, marker, first_move):
        super().__init__(name, marker, first_move)