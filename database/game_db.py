from . import db
from exceptions import GameNotFoundError

games = db["games"]

# Ensure the index is created on "game_id" for consistency
if "games" not in db.list_collection_names():
    games.create_index("game_id", unique=True)

def add_game(game: dict[str, str]) -> None:
    """Add a new game to the database."""
    if get_game(game["game_id"]):  # Consistent use of "game_id"
        raise ValueError("Game with this ID already exists.")
    print(f"Adding game {game['game_id']} to the database.")  # Updated to "game_id"
    games.insert_one(game)
    print(f"Game {game['game_id']} added to the database.")  # Updated to "game_id"

def get_game(game_id: str) -> dict[str, str]:
    """Fetch a game by its ID."""
    query_by_id = {"game_id": game_id}  # Consistent use of "game_id"
    print(f"Fetching game with ID {game_id}.")
    game = games.find_one(query_by_id)
    if not game:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")
    return game

def update_game_with_player(game_id: str, new_player: dict[str, str]) -> dict:
    """Update an existing game in the database."""
    query_by_id = {"game_id": game_id}  # Consistent use of "game_id"
    update_data = {"$push": {"players": new_player}}
    print(f"Updating game {game_id} with new player {new_player['name']}.")
    game = games.update_one(query_by_id, update_data)
    if game.matched_count == 0:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")
    return get_game(game_id)