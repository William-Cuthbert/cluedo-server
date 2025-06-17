import uuid
from entity.player import Player

class Game:
    def __init__(self, players: list[Player] = None, case_file: dict[str, str] = None, 
                 cards: list[str] = None, state: str = None, current_turn: str = None, 
                 turn_over: list[str] = None):
        self._game_id = str(uuid.uuid4())
        self._players = players or []
        self._case_file = case_file or {}
        self._cards = cards or []
        self._state = state
        self._current_turn = current_turn
        self._turn_over = turn_over or []
    
    @property
    def game_id(self) -> str:
        return self._game_id
    
    @property
    def players(self) -> list[Player]:
        return self._players
    
    @players.setter
    def players(self, players: list[Player]):
        self._players = players
    
    @property
    def case_file(self) -> dict[str, str]:
        return self._case_file
    
    @case_file.setter
    def case_file(self, case_file):
        self._case_file = case_file
        
    @property
    def cards(self) -> list[str]:
        return self._cards
    
    @cards.setter
    def cards(self, cards):
        self._cards = cards
        
    @property
    def state(self) -> str:
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state
        
    @property
    def current_turn(self) -> str:
        return self._current_turn
    
    @current_turn.setter
    def current_turn(self, current_turn):
        self._current_turn = current_turn
    
    @property
    def turn_over(self) -> list[str]:
        return self._turn_over
    
    @turn_over.setter
    def turn_over(self, turn_over):
        self._turn_over = turn_over
    
    def add_player(self, player: Player):
        """Adds a player to the game."""
        if player not in self._players:
            self._players.append(player)
            player.add_game(self)
    
    def __repr__(self):
        return f"Game({self._game_id}, {self._players}, {self._case_file}, {self._cards}, {self._state}, {self._current_turn}, {self._turn_over})"
    
    def __hash__(self):
        return hash(self._game_id)