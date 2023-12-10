class Game:
    def __init__(self):
        self.board = [[[['_'] * 3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.next_board = None
        self.move_history = []

    def make_move(self, board, cell):
        board_row, board_col = board
        button_row, button_col = cell
        if self.next_board is not None and self.next_board != (board_row, board_col):
            return False
        try:
            if self.board[board_row][board_col][button_row][button_col] != '_':
                return False
            self.board[board_row][board_col][button_row][button_col] = self.current_player
            self.next_board = (button_row, button_col)
            self.move_history.append((board, cell))
            return True
        except IndexError:
            pass

    def check_winner(self, player):
        for board_row in range(3):
            for board_col in range(3):
                for i in range(3):
                    if self.board[board_row][board_col][i][0] == self.board[board_row][board_col][i][1] == self.board[board_row][board_col][i][2] == player:
                        return True
                    if self.board[board_row][board_col][0][i] == self.board[board_row][board_col][1][i] == self.board[board_row][board_col][2][i] == player:
                        return True
                if self.board[board_row][board_col][0][0] == self.board[board_row][board_col][1][1] == self.board[board_row][board_col][2][2] == player:
                    return True
                if self.board[board_row][board_col][0][2] == self.board[board_row][board_col][1][1] == self.board[board_row][board_col][2][0] == player:
                    return True
                return False

    def get_all_possible_moves(self):
        moves = []
        for board_row in range(3):
            for board_col in range(3):
                for button_row in range(3):
                    for button_col in range(3):
                        if self.board[board_row][board_col][button_row][button_col] == '_':
                            moves.append(((board_row, board_col), (button_row, button_col)))
        return moves

    def undo_move(self, board, cell):
        if self.move_history:
            last_board, last_cell = self.move_history.pop()
            board_row, board_col = last_board
            button_row, button_col = last_cell
            self.board[board_row][board_col][button_row][button_col] = '_'
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def evaluate(self, player):
        for board_row in range(3):
            for board_col in range(3):
                for i in range(3):
                    if self.board[board_row][board_col][i][0] == self.board[board_row][board_col][i][1] == \
                            self.board[board_row][board_col][i][2] == player:
                        return 1
                    if self.board[board_row][board_col][0][i] == self.board[board_row][board_col][1][i] == \
                            self.board[board_row][board_col][2][i] == player:
                        return 1
                if self.board[board_row][board_col][0][0] == self.board[board_row][board_col][1][1] == \
                        self.board[board_row][board_col][2][2] == player:
                    return 1
                if self.board[board_row][board_col][0][2] == self.board[board_row][board_col][1][1] == \
                        self.board[board_row][board_col][2][0] == player:
                    return 1
        return 0