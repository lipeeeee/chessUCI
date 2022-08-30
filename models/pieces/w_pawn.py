import pygame
import os
from globals.globals import PIECES_HEIGHT, PIECES_WIDTH

class w_pawn:
    IMAGE = pygame.transform.scale(pygame.image.load(os.path.join("assets", "w_pawn.png")), (PIECES_WIDTH, PIECES_HEIGHT))
