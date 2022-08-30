import pygame, os
from globals.globals import PIECES_HEIGHT, PIECES_WIDTH

def load_image_piece(code):
    return pygame.transform.scale(pygame.image.load(os.path.join("assets", code + ".png")), (PIECES_WIDTH, PIECES_HEIGHT))
