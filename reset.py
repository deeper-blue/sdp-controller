import json
import client as cl
from square_piece import square_to_piece

# Close connection to robot
def close():
    cl.close()

# Function to select the appropriate move based on the json data (move_data)
# move_data has the form jsondata["history"][n], where n is the move identifier
def reset_board(square, piece_map):

    print(square)
    initial_position = piece_map[square]


    if square != initial_position:
        piece = square_to_piece[initial_position]

        rowA, colA = square[:1].upper(), int(square[1:])
        cellA = (rowA,colA)

        rowB, colB = initial_position[:1].upper(), int(initial_position[1:])
        cellB = (rowB,colB)

        cl.move_piece(cellA, cellB, piece)
        return initial_position
