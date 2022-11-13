from globals.coordinates import BOARD_COORDINATES, SQUARES_COORDINATES
from globals.globals import (BOARD_START_X, INT_TO_LETTER_DICT, SQUARES_HEIGHT,
                             SQUARES_WIDTH)
from models.piece import Piece


def reset_board()  :
    # White side pawns
    for i in range(8):
        BOARD_COORDINATES[INT_TO_LETTER_DICT.get(i + 1) + str(2)] = Piece("w_pawn")
    
    BOARD_COORDINATES["a1"] = Piece("w_rook")
    BOARD_COORDINATES["h1"] = Piece("w_rook")
    BOARD_COORDINATES["b1"] = Piece("w_knight")
    BOARD_COORDINATES["g1"] = Piece("w_knight")
    BOARD_COORDINATES["c1"] = Piece("w_bishop")
    BOARD_COORDINATES["f1"] = Piece("w_bishop")
    BOARD_COORDINATES["d1"] = Piece("w_queen")
    BOARD_COORDINATES["e1"] = Piece("w_king")

    # Black side pawns
    for i in range(8):
        BOARD_COORDINATES[INT_TO_LETTER_DICT.get(i + 1) + str(7)] = Piece("b_pawn")
    
    BOARD_COORDINATES["a8"] = Piece("b_rook")
    BOARD_COORDINATES["h8"] = Piece("b_rook")
    BOARD_COORDINATES["b8"] = Piece("b_knight")
    BOARD_COORDINATES["g8"] = Piece("b_knight")
    BOARD_COORDINATES["c8"] = Piece("b_bishop")
    BOARD_COORDINATES["f8"] = Piece("b_bishop")
    BOARD_COORDINATES["d8"] = Piece("b_queen")
    BOARD_COORDINATES["e8"] = Piece("b_king")

def get_square(pos):
    x, y = pos
    squareFound = None

    # Check if clicked on board
    if (x < BOARD_START_X + (8 * SQUARES_WIDTH) and
    x + (8 * SQUARES_WIDTH) > BOARD_START_X):
        
        for square, coordinates in SQUARES_COORDINATES.items():
            # ABBA colision algorithm
            if (x < coordinates[0] + SQUARES_WIDTH and
            x + SQUARES_WIDTH > coordinates[0] and
            y < coordinates[1] + SQUARES_HEIGHT and
            y + SQUARES_HEIGHT > coordinates[1]):
                squareFound = square            

    return squareFound