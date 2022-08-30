import os
import globals.coordinates as coordinates
from models.pieces.w_pawn import w_pawn
import pygame, renderer
import globals.globals as globals, globals.colors as colors

# Setup game window
WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))
pygame.display.set_caption(globals.WINDOW_CAPTION)

def game_loop():
    running = True
    clock = pygame.time.Clock()

    renderer.draw_window(WIN, colors.BLACK)
    renderer.draw_board(WIN)

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