import pygame
from globals.coordinates import SQUARES_COORDINATES
from globals.globals import HEIGHT, SQUARES_HEIGHT, SQUARES_WIDTH, WIDTH
from models.s_white import s_white
from models.s_black import s_black

def draw_window(WIN, color):
    WIN.fill(color)
    pygame.display.update()

def draw_obj(WIN, obj, x, y):
    WIN.blit(obj, (x, y))
    pygame.display.update()

# Draws board from a1 to h8 and calculates coordinates for all squares
def draw_board(WIN):
    BOARD_START_X, BOARD_START_Y = 50, HEIGHT - SQUARES_HEIGHT
    cur_x, cur_y = BOARD_START_X, BOARD_START_Y

    white = True # Flag to know wether to render white or black squares
    letter_to_int_dict = {
        1: "a", 2: "b", 3: "c",
        4: "d", 5: "e", 6: "f",
        7: "g", 8: "h"
    }

    for i in range(8):
        for j in range(8):
            if white:
                draw_obj(WIN, s_white.IMAGE, cur_x, cur_y)
            else:
                draw_obj(WIN, s_black.IMAGE, cur_x, cur_y)

            white = not white
            cur_x += SQUARES_WIDTH

            # TODO: FIX H3 H4 SQUARES
            # Map coords
            SQUARES_COORDINATES[str(letter_to_int_dict.get(j + 1) + str(i + 1))] = (cur_x, cur_y)

        white = not white
        cur_y -= SQUARES_HEIGHT
        cur_x = BOARD_START_X 

    print(SQUARES_COORDINATES)
