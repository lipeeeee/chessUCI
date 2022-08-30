import pygame
from globals.coordinates import BOARD_COORDINATES, SQUARES_COORDINATES
from globals.globals import BOARD_START_X, SQUARES_HEIGHT, SQUARES_WIDTH, BOARD_START_Y
from models.pieces import PIECES_DATABASE
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
    cur_x, cur_y = BOARD_START_X, BOARD_START_Y
    white = True # Flag to know wether to render white or black squares
    int_to_letter_dict = {
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

            # Map coords
            SQUARES_COORDINATES[str(int_to_letter_dict.get(j + 1) + str(i + 1))] = (cur_x, cur_y)

        white = not white
        cur_y -= SQUARES_HEIGHT
        cur_x = BOARD_START_X 

    print(SQUARES_COORDINATES)

def draw_pieces(WIN):
    #TODO : FIX PIECES RENDERING ONE SQUARE_WIDTH ABOVE THAN THEY SHOULD

    for board_coordinate in BOARD_COORDINATES.items():
        if board_coordinate[1] != "":
            print("Rendering pawn at: " + str(SQUARES_COORDINATES[board_coordinate[0]][0]) + ", " + str(SQUARES_COORDINATES[board_coordinate[0]][1]))
            draw_obj(WIN, PIECES_DATABASE[board_coordinate[1]], SQUARES_COORDINATES[board_coordinate[0]][0], SQUARES_COORDINATES[board_coordinate[0]][1])
