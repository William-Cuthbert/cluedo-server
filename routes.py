from flask import Blueprint, jsonify, request
from model import create_game
from exceptions import GameNotFoundError, GameFullError

cluedo_routes = Blueprint('cluedo_routes', __name__)

@cluedo_routes.route('/create_game', methods=['POST'])
def start_game():
    new_game = create_game()
    return jsonify({new_game}), 201

@cluedo_routes.route('/join_game', methods=['POST'])
def join_game():
    data = request.get_json()
    game_id = data.get('game_id')
    player_name = data.get('player_name')
    if not game_id or not player_name:
        return jsonify({"error": "Game ID and player name are required."}), 400
    try:
        game = join_game(game_id, player_name)
        return jsonify(game), 200
    except GameNotFoundError as e:
        return jsonify({"error": str(e)}), 404
    except GameFullError as e:
        return jsonify({"error": str(e)}), 400
