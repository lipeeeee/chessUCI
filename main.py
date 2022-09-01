import pygame
pygame.init()
import globals.coordinates as coordinates
import utils.board_utils as board_utils
import renderer
import globals.globals as globals, globals.colors as colors

# Setup game window
WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
WIN.fill(colors.BLACK)
pygame.display.set_caption(globals.WINDOW_CAPTION)

highlited_piece = None

# Events
PIECE_SELECTED = pygame.USEREVENT + 1

def game_loop():
    # Setup backend
    running = True
    clock = pygame.time.Clock()
    global highlited_piece

    # Setup window
    board_utils.reset_board()
    renderer.draw_window(WIN)

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
                    highlite_piece(board_utils.get_square(pygame.mouse.get_pos()))

            elif event.type == PIECE_SELECTED:
                # TODO: show legal moves

                if highlited_piece != None:
                    pass

                pass


    pygame.quit()

def highlite_piece(piece):
    global highlited_piece
    highlited_piece = piece

    # Draw board with the highlited piece
    renderer.draw_board(WIN, highlited_piece)
    renderer.draw_pieces(WIN)
    renderer.draw_coordinates(WIN)

    renderer.draw_highlited_piece_text(WIN, highlited_piece)

    pygame.event.post(pygame.event.Event(PIECE_SELECTED))


if __name__ == '__main__':
    game_loop()