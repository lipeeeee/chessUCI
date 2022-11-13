from models.square import Square

SQUARES_DATABASE = {
    "w_square": Square("s_white"),
    "b_square": Square("s_black"),
    "h_square": Square("s_highlited"),
    "w_lm_square": Square("s_white_legal_move"),
    "b_lm_square": Square("s_black_legal_move"),
    "lm_square" : Square("lm_square")
}