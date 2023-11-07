import sys
import pygame
import pygame as pg

pg.init()
size_button = 100
margin = 15
width = size_button * 3 + margin * 4
height = width
size_window = (width, height)
screen = pg.display.set_mode(size_window)
pg.display.set_caption("Крестики нолики")
PLAYER = "X"
COMPUTER = "O"
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
mas = [['_'] * 3 for i in range(3)]
print(mas)


def minimax(board, depth, is_maximizing):
    result = check_winner()

    if result is not None:
        if result == COMPUTER:
            return 1
        elif result == PLAYER:
            return -1
        else:
            return 0

    if is_maximizing:
        best_score = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    board[row][col] = COMPUTER
                    score = minimax(board, depth + 1, False)
                    board[row][col] = '_'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col] == '_':
                    board[row][col] = PLAYER
                    score = minimax(board, depth + 1, True)
                    board[row][col] = '_'
                    best_score = min(score, best_score)
        return best_score


def best_move():
    best_score = -float('inf')
    move = None
    for row in range(3):
        for col in range(3):
            if mas[row][col] == '_':
                mas[row][col] = COMPUTER
                score = minimax(mas, 0, False)
                mas[row][col] = '_'
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move


def check_winner():
    # Проверка выигрышных комбинаций
    for i in range(3):
        if mas[i][0] == mas[i][1] == mas[i][2] != '_':
            return mas[i][0]
        if mas[0][i] == mas[1][i] == mas[2][i] != '_':
            return mas[0][i]
    if mas[0][0] == mas[1][1] == mas[2][2] != '_':
        return mas[0][0]
    if mas[0][2] == mas[1][1] == mas[2][0] != '_':
        return mas[0][2]
    return None


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (size_button + margin)
            row = y_mouse // (size_button + margin)
            if mas[row][col] == "_":
                if PLAYER == "X":
                    mas[row][col] = 'X'
                    PLAYER = "O"
                if check_winner() is None:
                    computer_move = best_move()
                    if computer_move:
                        row, col = computer_move
                        mas[row][col] = 'O'
                    PLAYER = "X"
    for row in range(3):
        for col in range(3):
            x = col * size_button + (col + 1) * margin
            y = row * size_button + (row + 1) * margin
            pg.draw.rect(screen, white, (x, y, size_button, size_button))
            if mas[row][col] == 'X':
                color = green
                symbol = 'X'
            elif mas[row][col] == 'O':
                color = red
                symbol = 'O'
            else:
                color = white
                symbol = ''
            pg.draw.rect(screen, color, (x, y, size_button, size_button))
            font = pg.font.Font(None, 36)
            text = font.render(symbol, True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + size_button // 2, y + size_button // 2))
            screen.blit(text, text_rect)
    pg.display.update()
