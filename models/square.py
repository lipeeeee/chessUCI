from utils.img_utils import load_image_square

class Square:

    def __init__(self, code):
        self.code = code
        self.image = load_image_square(self.code)

    def get_piece(self):
        return None