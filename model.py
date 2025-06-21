import random
from uuid import uuid4
from database import db
from database.game_db import add_game, get_game, update_game_with_player
from exceptions import GameFullError
from enums import Character, Room, Weapon, GameState

def generate_case_file() -> dict[str, str]:
    """Sets the case file"""
    return {
        "suspect": random.choice(list(Character)).value,
        "weapon": random.choice(list(Weapon)).value,
        "room": random.choice(list(Room)).value
    }

def distribute_cards(case_file: dict[str, str]) -> list[str]:
    """Distributes the remaining cards to players."""
    all_cards = list(Character) + list(Weapon) + list(Room)
    remaining_cards = [card.value for card in all_cards if card.value not in case_file.values()]
    random.shuffle(remaining_cards)
    return remaining_cards

def create_game() -> dict[str, str]:
    """Creates a new game."""
    game_id = str(uuid4())
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
    if game.get("state", None) != GameState.WAITING_FOR_PLAYERS.value:
        raise ValueError("Game is already in progress.")
    if len(game["players"]) >= 6:
        raise GameFullError("Game is full.")
    player = {
        "id": len(game["players"]) + 1,
        "player_id": str(uuid4()),
        "name": player_name,
        "cards": []
    }
    game = update_game_with_player(game_id, player)
    return game