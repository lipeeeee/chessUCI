import pygame
pygame.init()
from utils.text_utils import FONT_MONOSPACE
import globals.coordinates as coordinates
import renderer
import globals.globals as globals, globals.colors as colors
from models.pieces import load_image_piece

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

    # Setup window
    coordinates.reset_board()
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
                    # if click is on board and there is a piece on the square highlit the piece
                    highlited_piece = coordinates.get_square(pygame.mouse.get_pos())
                    pygame.event.post(pygame.event.Event(PIECE_SELECTED))

            elif event.type == PIECE_SELECTED:
                renderer.draw_highlited_piece(WIN, highlited_piece)


    pygame.quit()

if __name__ == '__main__':
    game_loop()