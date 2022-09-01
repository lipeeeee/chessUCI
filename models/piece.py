from globals.coordinates import BOARD_COORDINATES, SQUARES_COORDINATES
from globals.globals import PIECES_HEIGHT, PIECES_WIDTH
from renderer import draw_obj
from utils.img_utils import load_image_piece

class Piece:
    WIDTH, HEIGHT = PIECES_WIDTH , PIECES_HEIGHT

    def __init__(self, code):
        self.code = code

    def legal_moves(self):
        # TODO
        pass
