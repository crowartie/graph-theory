import pygame as pg
import sys
import concurrent.futures
from game import Game
from minimax import minimax
depth =3
maximizing_player = False
def minimax_with_args():
    return minimax(game, depth, maximizing_player)

pg.init()
margin = 5
board_size = 180
button_size = 55
width = height = board_size * 3 + margin * 4
size_window = (width, height)
screen = pg.display.set_mode(size_window)
pg.display.set_caption("Сложные крестики нолики")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

game = Game()
last_move = None

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            board_col = x // board_size
            board_row = y // board_size
            button_col = (x % board_size) // button_size
            button_row = (y % board_size) // button_size
            if game.make_move((board_row, board_col), (button_row, button_col)):
                print(f"Ход сделан на доске {board_row},{board_col} в ячейке {button_row},{button_col}")
                print(f"Следующий ход на доске {(button_row * 3 + button_col)+1}")
                if game.check_winner(game.current_player):
                    print(f"Победил {game.current_player}")
                game.current_player = 'O' if game.current_player == 'X' else 'X'
            else:
                print(f"Ход невозможен")
        if game.current_player == 'O':  # Если текущий игрок - это компьютер
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(minimax_with_args)
                try:
                    result = future.result(timeout=5)
                except concurrent.futures.TimeoutError:
                    print("Время вышло!")
    font = pg.font.Font(None, 24)
    for board_row in range(3):
        for board_col in range(3):
            for row in range(3):
                for col in range(3):
                    x = (col * button_size + (col + 1) * margin) + (
                            board_col * (board_size + margin))
                    y = (row * button_size + (row + 1) * margin) + (
                            board_row * (board_size + margin))
                    cell_row = row % 3
                    cell_col = col % 3
                    symbol = game.board[board_row][board_col][cell_row][cell_col]
                    if symbol == 'X':
                        color = GREEN
                    elif symbol == 'O':
                        color = RED
                    else:
                        color = WHITE
                    pg.draw.rect(screen, color, (x, y, button_size, button_size))
                    if symbol != '_':
                        font = pg.font.Font(None, 36)
                        text = font.render(symbol, True, BLACK)
                        text_rect = text.get_rect(center=(x + button_size // 2, y + button_size // 2))
                        screen.blit(text, text_rect)
    pg.display.update()
