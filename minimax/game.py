class Game:
    PLAYER = "X"
    COMPUTER = "O"

    def __init__(self):
        self.board = [['_'] * 3 for _ in range(3)]
        self.active_turn = self.PLAYER

    def over(self):
        return self.check_winner() is not None or self.get_available_moves() == []

    def get_available_moves(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == '_']

    def get_new_state(self, move):
        new_game = Game()
        new_game.board = [row.copy() for row in self.board]
        new_game.board[move[0]][move[1]] = self.active_turn
        new_game.active_turn = self.COMPUTER if self.active_turn == self.PLAYER else self.PLAYER
        return new_game

    def win(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_winner(self):
        if self.win(self.PLAYER):
            return self.PLAYER
        if self.win(self.COMPUTER):
            return self.COMPUTER
        return None