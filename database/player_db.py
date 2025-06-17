from . import db

players = db["players"]

if "players" not in db.list_collection_names():
    players.create_index("id", unique=True)

def add_player(player):
    """Add a new player to the database."""
    try:
        players.insert_one(player)
    except Exception as e:
        print(f"Error adding player: {e}")
        raise

def get_player(player_id):
    """Fetch a player by its ID."""
    try:
        player = players.find_one({"id": player_id})
        return player if player else None
    except Exception as e:
        print(f"Error fetching player: {e}")
        raise