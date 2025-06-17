import random
from uuid import UUID
from database import db
from database.game_db import add_game, get_game, update_game_with_player
from exceptions import GameFullError

CHARACTERS = ("Professor Plum","Miss Scarlett","Mrs Peacock","Colonel Mustard","Reverend Green")
ROOMS = ("hall","study","ballroom","billiards","bedroom","dining room","kitchen","lounge","conservatory","library")
WEAPONS = ("candlestick","wrench","lead pipe","rope","dagger","revolver")

def generate_case_file() -> dict[str, str]:
    """Sets the case file"""
    return {
        "suspect": random.choice(CHARACTERS),
        "weapon": random.choice(WEAPONS),
        "room": random.choice(ROOMS)
    }

def distribute_cards(case_file: dict[str, str]) -> list[str]:
    """Distributes the remaining cards to players."""
    remaining_cards = [card for card in CHARACTERS + WEAPONS + ROOMS 
                       if card not in case_file.values()]
    random.shuffle(remaining_cards)
    return remaining_cards

def create_game() -> dict[str, str]:
    """Creates a new game."""
    game_id = UUID().str()
    case_file = generate_case_file()
    cards = distribute_cards(case_file)
    game = {
        "game_id": game_id,
        "players": [],
        "case_file": case_file,
        "cards": cards,
        "state": "waiting",
        "current_turn": None,
        "turn_over": []
    }
    add_game(game)
    return game

def join_game(game_id: str, player_name: str) -> dict[str, str]:
    """Adds a player to a new game."""
    game = get_game(game_id)
    if game.get("state", None) != "waiting":
        raise ValueError("Game is already in progress.")
    if len(game["players"]) >= 6:
        raise GameFullError("Game is full.")
    player = {
        "id": len(game["players"]) + 1,
        "player_id": UUID().str(),
        "name": player_name,
        "cards": []
    }
    game = update_game_with_player(game_id, player)
    return game