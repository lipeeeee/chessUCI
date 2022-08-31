import pygame
import globals.colors as colors
from globals.coordinates import BOARD_COORDINATES, SQUARES_COORDINATES
from globals.globals import BOARD_START_X, INT_TO_LETTER_DICT, SQUARES_HEIGHT, SQUARES_WIDTH, BOARD_START_Y
from models.pieces import PIECES_DATABASE, SQUARES_DATABASE
from utils.text_utils import FONT_BOARD_COORDINATES, FONT_MONOSPACE

def draw_obj(WIN, obj, x, y):
    WIN.blit(obj, (x, y))
    pygame.display.update()

# Draws board from a1 to h8 and calculates coordinates for all squares
def draw_board(WIN):  
    cur_x, cur_y = BOARD_START_X, BOARD_START_Y
    white = True # Flag to know wether to render white or black squares

    for i in range(8):
        for j in range(8):
            if white:
                draw_obj(WIN, SQUARES_DATABASE["s_white"], cur_x, cur_y)
            else:
                draw_obj(WIN, SQUARES_DATABASE["s_black"], cur_x, cur_y)

            white = not white
            cur_x += SQUARES_WIDTH

            # Map coords
            SQUARES_COORDINATES[str(INT_TO_LETTER_DICT.get(j + 1) + str(i + 1))] = (cur_x, cur_y)

        white = not white
        cur_y -= SQUARES_HEIGHT
        cur_x = BOARD_START_X 

def draw_pieces(WIN):
    #TODO : FIX PIECES RENDERING ONE SQUARE_WIDTH ABOVE THAN THEY SHOULD

    for board_coordinate in BOARD_COORDINATES.items():
        if board_coordinate[1] != "":
            # TEMPORARY FIX: MOVING THE PIECES 1 SQUARE_WIDTH BEHIND
            draw_obj(WIN, PIECES_DATABASE[board_coordinate[1]], SQUARES_COORDINATES[board_coordinate[0]][0] - SQUARES_WIDTH, SQUARES_COORDINATES[board_coordinate[0]][1])

def draw_coordinates(WIN):
    label = FONT_BOARD_COORDINATES.render("", 1, colors.WHITE)

    # Numbers
    cur_x, cur_y = BOARD_START_X, BOARD_START_Y
    for i in range(8):
        label = FONT_BOARD_COORDINATES.render(str(i + 1), 1, colors.BLACK)
        draw_obj(WIN, label, cur_x, cur_y)

        cur_y -= SQUARES_HEIGHT

    # Letters
    cur_x, cur_y = BOARD_START_X, BOARD_START_Y + (SQUARES_HEIGHT - 30)
    for i in range(8):
        label = FONT_BOARD_COORDINATES.render(str(INT_TO_LETTER_DICT.get(i + 1)), 1, colors.BLACK)
        draw_obj(WIN, label, cur_x, cur_y)

        cur_x += SQUARES_WIDTH

def draw_window(WIN):
    draw_board(WIN)
    draw_pieces(WIN)
    draw_coordinates(WIN)
    
    pygame.display.update()

def draw_highlited_piece(WIN, highlited_piece):
    x, y = BOARD_START_X + (SQUARES_WIDTH * 8) + 40, 15

    highlited_piece_text = FONT_MONOSPACE.render("HIGHLITED PIECE: " + str(highlited_piece), 1, colors.SATURATED_GREEN)
    pygame.draw.rect(WIN, colors.BLACK, pygame.Rect(x, y, 170, 20))
    draw_obj(WIN, highlited_piece_text, x, y)
    
    pygame.display.update()
