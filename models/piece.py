from globals.globals import PIECES_HEIGHT, PIECES_WIDTH

class Piece:
    WIDTH, HEIGHT = PIECES_WIDTH , PIECES_HEIGHT

    def __init__(self, code):
        self.code = code

    def legal_moves(self):
        # TODO
        pass
