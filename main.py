import pygame
import globals

WIN = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT))

def game_loop():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    game_loop()