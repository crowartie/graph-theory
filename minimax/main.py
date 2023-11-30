import sys
import pygame as pg
from game import Game
from minimax import minimax

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

game = Game()

def draw_endgame_message(result):
    if result == 'X':
        message = "Победили крестики!"
    elif result == 'O':
        message = "Победили нолики!"
    else:
        message = "Ничья!"
    font = pg.font.Font(None, 50)
    text = font.render(message, True, (0, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))


def reset_game():
    global game
    game = Game()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        elif event.type == pg.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pg.mouse.get_pos()
            col = x_mouse // (size_button + margin)
            row = y_mouse // (size_button + margin)
            if game.board[row][col] == "_":
                game.board[row][col] = 'X'
                winner = game.check_winner()
                if winner is not None or game.get_available_moves() == []:
                    draw_endgame_message(winner)
                    pg.display.update()
                    pg.time.wait(2000)
                    reset_game()
                else:
                    best_move_info = minimax(game, 0)
                    if best_move_info["move"]:
                        row, col = best_move_info["move"]
                        game.board[row][col] = 'O'
                        winner = game.check_winner()
                        if winner is not None or game.get_available_moves() == []:
                            draw_endgame_message(winner)
                            pg.display.update()
                            pg.time.wait(2000)
                            reset_game()
    for row in range(3):
        for col in range(3):
            x = col * size_button + (col + 1) * margin
            y = row * size_button + (row + 1) * margin
            pg.draw.rect(screen, white, (x, y, size_button, size_button))
            if game.board[row][col] == 'X':
                color = green
                symbol = 'X'
            elif game.board[row][col] == 'O':
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
