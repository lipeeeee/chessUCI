import pygame
import os
from globals.globals import SQUARES_HEIGHT, SQUARES_WIDTH

class s_white:
    IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "s_white.png")), (SQUARES_WIDTH, SQUARES_HEIGHT))