from globals.globals import SQUARES_HEIGHT, SQUARES_WIDTH, BOARD_START_X

# x, y of all squares
SQUARES_COORDINATES = {
    "a1": (()),
    "a2": (()),
    "a3": (()),
    "a4": (()),
    "a5": (()),
    "a6": (()),
    "a7": (()),
    "a8": (()),
    "b1": (()),
    "b2": (()),
    "b3": (()),
    "b4": (()),
    "b5": (()),
    "b6": (()),
    "b7": (()),
    "b8": (()),
    "c1": (()),
    "c2": (()),
    "c3": (()),
    "c4": (()),
    "c5": (()),
    "c6": (()),
    "c7": (()),
    "c8": (()),
    "d1": (()),
    "d2": (()),
    "d3": (()),
    "d4": (()),
    "d5": (()),
    "d6": (()),
    "d7": (()),
    "d8": (()),
    "e1": (()),
    "e2": (()),
    "e3": (()),
    "e4": (()),
    "e5": (()),
    "e6": (()),
    "e7": (()),
    "e8": (()),
    "f1": (()),
    "f2": (()),
    "f3": (()),
    "f4": (()),
    "f5": (()),
    "f6": (()),
    "f7": (()),
    "f8": (()),
    "g1": (()),
    "g2": (()),
    "g3": (()),
    "g4": (()),
    "g5": (()),
    "g6": (()),
    "g7": (()),
    "g8": (()),
    "h1": (()),
    "h2": (()),
    "h3": (()),
    "h4": (()),
    "h5": (()),
    "h6": (()),
    "h7": (()),
    "h8": (()),
}

# x, y of all pieces
BOARD_COORDINATES = {
    "a1": "",
    "a2": "",
    "a3": "",
    "a4": "",
    "a5": "",
    "a6": "",
    "a7": "",
    "a8": "",
    "b1": "",
    "b2": "",
    "b3": "",
    "b4": "",
    "b5": "",
    "b6": "",
    "b7": "",
    "b8": "",
    "c1": "",
    "c2": "",
    "c3": "",
    "c4": "",
    "c5": "",
    "c6": "",
    "c7": "",
    "c8": "",
    "d1": "",
    "d2": "",
    "d3": "",
    "d4": "",
    "d5": "",
    "d6": "",
    "d7": "",
    "d8": "",
    "e1": "",
    "e2": "",
    "e3": "",
    "e4": "",
    "e5": "",
    "e6": "",
    "e7": "",
    "e8": "",
    "f1": "",
    "f2": "",
    "f3": "",
    "f4": "",
    "f5": "",
    "f6": "",
    "f7": "",
    "f8": "",
    "g1": "",
    "g2": "",
    "g3": "",
    "g4": "",
    "g5": "",
    "g6": "",
    "g7": "",
    "g8": "",
    "h1": "",
    "h2": "",
    "h3": "",
    "h4": "",
    "h5": "",
    "h6": "",
    "h7": "",
    "h8": "",
}

def reset_board():
    int_to_letter_dict = {
        1: "a", 2: "b", 3: "c",
        4: "d", 5: "e", 6: "f",
        7: "g", 8: "h"
    }

    # White side pawns
    for i in range(8):
        BOARD_COORDINATES[int_to_letter_dict.get(i + 1) + str(2)] = "w_pawn"
        

def get_square(pos):
    x, y = pos
    squareFound = None

    # Check if clicked on board
    if (x < BOARD_START_X + (8 * SQUARES_WIDTH) and
    x + (8 * SQUARES_WIDTH) > BOARD_START_X):
        
        #print("POSITION CLICKED: " + str(pos))
        for square, coordinates in SQUARES_COORDINATES.items():
            # ABBA colision algorithm
            if (x < coordinates[0] + SQUARES_WIDTH and
            x + SQUARES_WIDTH > coordinates[0] and
            y < coordinates[1] + SQUARES_HEIGHT and
            y + SQUARES_HEIGHT > coordinates[1]):
                squareFound = square            

    return squareFound