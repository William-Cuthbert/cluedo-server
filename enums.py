from enum import Enum

class GameState(Enum):
    WAITING_FOR_PLAYERS = "waiting_for_players"
    IN_PROGRESS = "in_progress"
    PAUSED = "paused"
    COMPLETED = "completed"
    
class Character(Enum):
    PROFESSOR_PLUM = "Professor Plum"
    MISS_SCARLETT = "Miss Scarlett"
    MRS_PEACOCK = "Mrs Peacock"
    COLONEL_MUSTARD = "Colonel Mustard"
    REVEREND_GREEN = "Reverend Green"

class Room(Enum):
    HALL = "Hall"
    STUDY = "Study"
    BALLROOM = "Ballroom"
    BILLIARDS = "Billiards"
    BEDROOM = "Bedroom"
    DINING_ROOM = "Dining room"
    KITCHEN = "Kitchen"
    LOUNGE = "Lounge"
    CONSERVATORY = "Conservatory"
    LIBRARY = "Library"

class Weapon(Enum):
    CANDLESTICK = "Candlestick"
    WRENCH = "Wrench"
    LEAD_PIPE = "Lead pipe"
    ROPE = "Rope"
    DAGGER = "Dagger"
    REVOLVER = "Revolver"