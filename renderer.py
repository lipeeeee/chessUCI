import pygame
import globals.colors as colors
from globals.coordinates import BOARD_COORDINATES, SQUARES_COORDINATES
from globals.globals import BOARD_START_X, INT_TO_LETTER_DICT, SQUARES_HEIGHT, SQUARES_WIDTH, BOARD_START_Y
from globals.global_models import SQUARES_DATABASE as SQUARES_DATABASE
from utils.img_utils import load_image_piece, load_image_square
from utils.text_utils import FONT_BOARD_COORDINATES, FONT_MONOSPACE

def draw_obj(WIN, obj, x, y):
    WIN.blit(obj, (x, y))
    pygame.display.update()

# Draws board from a1 to h8 and calculates coordinates for all squares
def draw_board(WIN, highlited_square, legal_moves):  
    cur_x, cur_y = BOARD_START_X, BOARD_START_Y
    white = True # Flag to know wether to render white or black squares
    
    for i in range(8):
        for j in range(8):
            square_code = str(INT_TO_LETTER_DICT.get(j + 1) + str(i + 1))

            if square_code == highlited_square:
                draw_obj(WIN, load_image_square(SQUARES_DATABASE["h_square"].code), cur_x, cur_y)
            elif legal_moves is not None and square_code in legal_moves:
                if white:
                    draw_obj(WIN, load_image_square(SQUARES_DATABASE["w_lm_square"].code), cur_x, cur_y)
                else:
                    draw_obj(WIN, load_image_square(SQUARES_DATABASE["b_lm_square"].code), cur_x, cur_y)
            elif white:
                draw_obj(WIN, load_image_square(SQUARES_DATABASE["w_square"].code), cur_x, cur_y)
            else:
                draw_obj(WIN, load_image_square(SQUARES_DATABASE["b_square"].code), cur_x, cur_y)

            white = not white
            cur_x += SQUARES_WIDTH

            # Map coords
            SQUARES_COORDINATES[square_code] = (cur_x, cur_y)

        white = not white
        cur_y -= SQUARES_HEIGHT
        cur_x = BOARD_START_X 

    draw_pieces(WIN)
    draw_coordinates(WIN)

def draw_pieces(WIN):
    for board_coordinate in BOARD_COORDINATES.items():
        if board_coordinate[1] != None:
            piece = board_coordinate[1]
            square_x, square_y = SQUARES_COORDINATES[board_coordinate[0]][0] - SQUARES_WIDTH, SQUARES_COORDINATES[board_coordinate[0]][1]

            draw_obj(WIN, load_image_piece(piece.code), square_x, square_y)

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

def draw_highlited_piece_text(WIN, highlited_piece):
    x, y = BOARD_START_X + (SQUARES_WIDTH * 8) + 40, 15

    highlited_piece_text = FONT_MONOSPACE.render("HIGHLITED PIECE: " + str(highlited_piece), 1, colors.SATURATED_GREEN)
    pygame.draw.rect(WIN, colors.BLACK, pygame.Rect(x, y, 190, 20))
    draw_obj(WIN, highlited_piece_text, x, y)

def draw_legal_moves_text(WIN, legal_moves):
    x, y = BOARD_START_X + (SQUARES_WIDTH * 8) + 40, 30

    legal_moves_text = FONT_MONOSPACE.render("LEGAL MOVES: " + str(legal_moves), 1, colors.SATURATED_GREEN)
    pygame.draw.rect(WIN, colors.BLACK, pygame.Rect(x, y, 230, 20))
    draw_obj(WIN, legal_moves_text, x, y)