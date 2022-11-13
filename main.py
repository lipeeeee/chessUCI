import pygame

pygame.init()
import globals.colors as colors
import globals.globals as globals
import piece_logic
import renderer
import utils.board_utils as board_utils

# Setup game window
WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
WIN.fill(colors.BLACK)
pygame.display.set_caption(globals.WINDOW_CAPTION)

highlited_square = None

# Events
PIECE_SELECTED = pygame.USEREVENT + 1

def game_loop():
    # Setup backend
    running = True
    clock = pygame.time.Clock()
    global highlited_square

    # Setup window
    board_utils.reset_board()
    renderer.draw_board(WIN, None, None)

    while running:
        # Make sure the FPS_CAP is being respected
        clock.tick(globals.FPS_CAP)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Left Click
                if event.button == 1:
                    # if click is on board and there is a piece on the square highlite the piece
                    highlite_square(board_utils.get_square(pygame.mouse.get_pos()))

            elif event.type == PIECE_SELECTED:
                legal_moves = piece_logic.get_legal_moves(highlited_square)
                renderer.draw_legal_moves_text(WIN, legal_moves)


    pygame.quit()

def highlite_square(square):
    global highlited_square
    highlited_square = square

    # Draw board with the highlited piece and legal moves
    legal_moves = piece_logic.get_legal_moves(highlited_square)
    renderer.draw_board(WIN, highlited_square, legal_moves)

    renderer.draw_highlited_piece_text(WIN, highlited_square)
    pygame.event.post(pygame.event.Event(PIECE_SELECTED))


if __name__ == '__main__':
    game_loop()