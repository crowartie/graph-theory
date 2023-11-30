from game import Game
PLAYER = "X"
COMPUTER = "O"


def calculate_score(game, depth):
    if game.win(PLAYER):
        return 10 - depth
    elif game.win(COMPUTER):
        return depth - 10
    else:
        return 0


def minimax(game, depth):
    if game.over():
        return {"depth": depth, "score": calculate_score(game, depth), "move": None, "submoves": []}
    depth += 1
    moves_info = []

    for move in game.get_available_moves():
        possible_game = game.get_new_state(move)
        move_info = minimax(possible_game, depth)
        move_info["move"] = move
        moves_info.append(move_info)

    if game.active_turn == PLAYER:
        best_move_info = max(moves_info, key=lambda x: x["score"])
    else:
        best_move_info = min(moves_info, key=lambda x: x["score"])

    return {"depth": depth, "score": best_move_info["score"], "move": best_move_info["move"], "submoves": moves_info}
