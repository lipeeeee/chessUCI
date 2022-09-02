from globals.coordinates import BOARD_COORDINATES
from models.piece import Piece


def get_legal_moves(square_code):
    legal_moves = []

    # Check if piece exists in square
    if square_code == None or BOARD_COORDINATES[square_code] == None:
        return legal_moves # None

    piece_code = BOARD_COORDINATES[square_code].code

    match piece_code:
        # Pawns can go up 2 squares(b2-b4)
        case 'w_pawn':
            for i in range(2):
                next_square = square_code[0] + str(int(square_code[1]) + i + 1)
                
                # Check if square not occupied
                if BOARD_COORDINATES[next_square] == None:
                    legal_moves.append(next_square)

        case 'b_pawn':
            for i in range(2):
                next_square = square_code[0] + str(int(square_code[1]) - (i + 1))

                # Check if square not occupied
                if BOARD_COORDINATES[next_square] == None:
                    legal_moves.append(next_square)
    

    return legal_moves