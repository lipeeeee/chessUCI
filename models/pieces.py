from utils.img_utils import load_image_piece, load_image_square

# Pieces dictionary, code & img
PIECES_DATABASE = {
    "w_pawn": load_image_piece("w_pawn"),
    "w_rook": load_image_piece("w_rook"),
    "w_bishop": load_image_piece("w_bishop"),
    "w_queen": load_image_piece("w_queen"),
    "w_king": load_image_piece("w_king"),
    "w_knight": load_image_piece("w_knight"),

    "b_pawn": load_image_piece("b_pawn"),
    "b_rook": load_image_piece("b_rook"),
    "b_bishop": load_image_piece("b_bishop"),
    "b_queen": load_image_piece("b_queen"),
    "b_king": load_image_piece("b_king"),
    "b_knight": load_image_piece("b_knight")
}

SQUARES_DATABASE = {
    "s_white": load_image_square("s_white"),
    "s_black": load_image_square("s_black")
}
