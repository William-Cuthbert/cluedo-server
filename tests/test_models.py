import unittest
from model import generate_case_file, distribute_cards, create_game, join_game, games, CHARACTERS, WEAPONS, ROOMS

class TestModels(unittest.TestCase):
    def test_generate_case_file(self):
        case_file = generate_case_file()
        self.assertIn(case_file['suspect'], CHARACTERS)
        self.assertIn(case_file['weapon'], WEAPONS)
        self.assertIn(case_file['room'], ROOMS)

    def test_distribute_cards(self):
        cards = distribute_cards()
        for card in cards:
            self.assertIsNotNone(card)

    def test_create_game(self):
        response = create_game()
        self.assertIsNotNone(response)
        self.assertIn("game_id", response)
        self.assertIn("players", response)
        self.assertIn("case_file", response)
        self.assertIn("cards", response)
        self.assertIn("state", response)
        self.assertIn("current_turn", response)
        self.assertIn("turn_over", response)

    def test_join_game(self):
        game = create_game()
        game_id = game["game_id"]
        player_name = "Player 1"
        response = join_game(game_id, player_name)
        player_name = "Player 2"
        response = join_game(game_id, player_name)
        self.assertEqual(2, len(response["players"]))
        for player in response["players"]:
            self.assertIsNotNone(player)
        

if __name__ == "__main__":
    unittest.main()