from . import db
from exceptions import GameNotFoundError

games = db["games"]

if "games" not in db.list_collection_names():
    games.create_index("id", unique=True)

def add_game(game: dict[str, str]) -> None:
    """Add a new game to the database."""
    if get_game(game["id"]):
        raise ValueError("Game with this ID already exists.")
    print(f"Adding game {game['id']} to the database.")
    games.insert_one(game)
    print(f"Game {game['id']} added to the database.")

def get_game(game_id: str) -> dict[str, str]:
    """Fetch a game by its ID."""
    query_by_id = {"id": game_id}
    print(f"Fetching game with ID {game_id}.")
    game = games.find_one(query_by_id)
    if not game:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")
    return game

def update_game_with_player(game_id: str, new_player: dict[str, str]) -> dict:
    """Update an existing game in the database."""
    query_by_id = {"id": game_id}
    update_data = {"$push": {"players": new_player}}
    print(f"Updating game {game_id} with new player {new_player['name']}.")
    game = games.update_one(query_by_id, update_data)
    if game.matched_count == 0:
        raise GameNotFoundError(f"Game with ID {game_id} not found.")
    return get_game(game_id)
