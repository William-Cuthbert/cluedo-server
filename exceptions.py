class GameNotFoundError(Exception):
    def __init__(self, game_id):
        self.game_id = game_id
        super().__init__(f"Game with ID {game_id} does not exist.")

class GameFullError(Exception):
    def __init__(self, game_id, max_players=6):
        self.game_id = game_id
        self.max_players = max_players
        super().__init__(f"Game with ID {game_id} is full. Maximum players allowed: {max_players}.")