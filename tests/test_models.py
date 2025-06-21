import unittest
from unittest.mock import patch, MagicMock
from model import generate_case_file, distribute_cards, create_game, join_game
from enums import Character, Weapon, Room, GameState

class TestModels(unittest.TestCase):
    def test_generate_case_file(self):
        case_file = generate_case_file()
        self.assertIn(case_file['suspect'], [character.value for character in Character])
        self.assertIn(case_file['weapon'], [weapon.value for weapon in Weapon])
        self.assertIn(case_file['room'], [room.value for room in Room])

    def test_distribute_cards(self):
        case_file = generate_case_file()
        cards = distribute_cards(case_file)
        all_cards = [character.value for character in Character] + \
                    [weapon.value for weapon in Weapon] + \
                    [room.value for room in Room]
        remaining_cards = [card for card in all_cards if card not in case_file.values()]
        self.assertEqual(len(cards), len(remaining_cards))
        self.assertEqual(sorted(cards), sorted(remaining_cards))
        for card in cards:
            self.assertIsNotNone(card)

    def test_create_game(self):
        with patch("model.get_game") as mock_get_game, \
             patch("model.add_game") as mock_add_game:
            mock_get_game.return_value = None
            mock_add_game.return_value = None
            response = create_game()
            self.assertIsNotNone(response)
            self.assertIn("game_id", response)
            self.assertIn("players", response)
            self.assertIn("case_file", response)
            self.assertIn("cards", response)
            self.assertIn("state", response)
            self.assertIn("current_turn", response)
            self.assertIn("turn_over", response)
            mock_add_game.assert_called_once_with(response)

    def test_join_game(self):
        game_id = "test_game_id"
        initial_game = {
            "game_id": game_id,
            "state": GameState.WAITING_FOR_PLAYERS.value,
            "players": [{"name": "Player 1"}]
        }

        with patch("model.get_game") as mock_get_game, \
            patch("model.update_game_with_player") as mock_update_game_with_player:
            # Mock initial game fetch
            mock_get_game.side_effect = [initial_game,  # Before Player 1 joins
                                        {**initial_game, "players": [{"name": "Player 1"}]},  # After Player 1 joins
                                        {**initial_game, "players": [{"name": "Player 1"}, {"name": "Player 2"}]}]  # After Player 2 joins

            # Mock update_game_with_player to return updated game
            mock_update_game_with_player.side_effect = lambda game_id, player: {
                **initial_game,
                "players": initial_game["players"] + [player]
            }

            # Join with Player 1
            player_name = "Player 1"
            response = join_game(game_id, player_name)
            self.assertIn(player_name, [player["name"] for player in response["players"]])

            # Join with Player 2
            player_name = "Player 2"
            response = join_game(game_id, player_name)
            self.assertEqual(2, len(response["players"]))
            for player in response["players"]:
                self.assertIsNotNone(player)
        
if __name__ == "__main__":
    unittest.main()