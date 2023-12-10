def minimax(game, depth, maximizing_player):
    if depth == 0 or game.check_winner(game.current_player):
        return game.evaluate(game.current_player)
    if maximizing_player:
        max_eval = float('-inf')
        for move in game.get_all_possible_moves():
            game.make_move(*move)
            eval = minimax(game, depth - 1, False)
            game.undo_move(*move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in game.get_all_possible_moves():
            game.make_move(*move)
            eval = minimax(game, depth - 1, True)
            game.undo_move(*move)
            min_eval = min(min_eval, eval)
        return min_eval

