import uuid
from entity.game import Game

class Player:
    def __init__(self, name: str, games_played: list[Game] = None, cards: list[str] = None, 
                 won: int = 0, losses: int = 0):
        self._player_id = str(uuid.uuid4())
        self._name = name
        self._games_played = games_played or []
        self._cards = cards or []
        self._won = won
        self._losses = losses
    
    @property
    def player_id(self) -> str:
        return self._player_id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def games_played(self) -> list[Game]:
        return self._games_played
    
    @games_played.setter
    def games_played(self, games_played: list[Game]):
        self._games_played = games_played
    
    @property
    def cards(self) -> list[str]:
        return self._cards
    
    @cards.setter
    def cards(self, cards: list[str]):
        self._cards = cards
    
    @property
    def won(self) -> int:
        return self._won
    
    @won.setter
    def won(self, won: int):
        """Sets the number of wins"""
        if won < 0:
            raise ValueError("Number of games won cannot be negative")
        self._won = won
    
    @property
    def losses(self) -> int:
        return self._losses
    
    @losses.setter
    def losses(self, losses: int):
        """Sets the number of losses"""
        if losses < 0:
            raise ValueError("Number of games lost cannot be negative")
        self._losses = losses
        
    def add_game(self, game: Game):
        """Adds a game to the player's list of played games."""
        if game not in self._games_played:
            self._games_played.append(game)
            game.add_player(self)

    def __str__(self):
        return f"Player(name={self.name}, score={self.score})"

    def __repr__(self):
        return self.__str__()