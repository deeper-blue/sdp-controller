import sys
import communication
import time
import json
import internal_logic
from controller_config import config
import client as cl
from square_piece import square_to_piece

# Arguably dangerous to assume these exist, but OK to crash if they don't
# since these values are necessary
version = config['controller']['version']
controller_id = config['controller']['id']


req = communication.Requester(controller_id, version)

def control_loop():

    ply_count = 0

    while True:
        t0 = time.time()
        r = req.sendResponse(ply_count)
        if r.status_code == 200:
            t1 = time.time()
            print("Got response: {}s".format(t1 - t0))
            jsonfile = r.json()
            print(jsonfile)

            if(jsonfile['game_over']['game_over']) {
                piece_list = ["a1","b1","c1","d1","e1","f1","g1","h1",
                "a2","b2","c2","d2","e2","f2","g2","h2",
                "a7","b7","c7","d7","e7","f7","g7","h7",
                "a8","b8","c8","d8","e8","f8","g8","h8",]
                for square, i in enumerate(jsonfile["initial_positions"]):
                    initial_position = reset.reset_board(square, jsonfile['initial_positions'])
                    piece_list.remove(initial_position)
                if piece_list != None:
                    for initial_pos, i in enumerate(piece_list):
                        col, row = square[:1].upper(), int(square[1:])
                        cell = (col,row)
                        buffer_cell = (8 + (row % 4), col
                        piece = square_to_piece[initial_pos]
                        cl.move_piece(buffer_cell, cell, piece)
                break
            }

            for actions, i in enumerate(jsonfile["history"]):
                ply_count = internal_logic.parseJson(jsonfile["history"][actions],ply_count)
                r = req.sendResponse(ply_count)
                print(r)

            time.sleep(10)
            t2 = time.time()
            print("Took: {}s".format(t2 - t0))
            print("\n")

try:
    control_loop()
except KeyboardInterrupt:
    internal_logic.close()
    sys.exit(0)

# Close robot connection
internal_logic.close()
