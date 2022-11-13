import os
import pygame
from globals.globals import (PIECES_HEIGHT, PIECES_WIDTH, SQUARES_HEIGHT,
                             SQUARES_WIDTH)


def load_image_piece(code):
    return pygame.transform.scale(pygame.image.load(os.path.join("assets", code + ".png")), (PIECES_WIDTH, PIECES_HEIGHT))

def load_image_square(code):
    return pygame.transform.scale(pygame.image.load(os.path.join("assets", code + ".png")), (SQUARES_WIDTH, SQUARES_HEIGHT))