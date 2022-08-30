import globals.coordinates as coordinates
import pygame, renderer
import globals.globals as globals, globals.colors as colors
from models.pieces import load_image_piece

# Setup game window
WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption(globals.WINDOW_CAPTION)

def game_loop():
    running = True
    clock = pygame.time.Clock()

    renderer.draw_window(WIN, colors.BLACK)

    # setup board
    coordinates.reset_board()
    renderer.draw_board(WIN)
    renderer.draw_pieces(WIN)

    while running:
        # Make sure the FPS_CAP is being respected
        clock.tick(globals.FPS_CAP)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Left Click
                if event.button == 1:
                    print(str(coordinates.get_square(pygame.mouse.get_pos())))

    pygame.quit()

if __name__ == '__main__':
    game_loop()