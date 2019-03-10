import json
import client as cl

with open('test.json') as f:
    data = json.load(f)

# Function to select the appropriate move based on the json data (move_data)
# move_data has the form jsondata["history"][n], where n is the move identifier
def parseJson(move_data, plycount):

    if (move_data["game_over"]["game_over"]):
        return "Game has finished"

    if (move_data==None):
        return "Data empty"

    _from = move_data["from"]
    to = move_data["to"]

    rowA, colA = _from[:1], int(_from[1:])
    cellA = (rowA,colA)

    rowB, colB = to[:1], int(to[1:])
    cellB = (rowB,colB)

    # Do take_piece
    if(move_data["capture"]["capture"]):
        piece = move_data["capture"]["capture"]["piece"]

        rowP, colP = piece[:1], int(piece[1:])
        piece_cell = (rowP,colP)

        cl.take_piece(cellA, cellB, piece)
        plycount+=1
        return ("", plycount)

    # Do castling
    elif(move_data["castle"]["castle"]):
        if (move_data["castle"]["side"]=='k'):
            cellC = (ord(cellA[0]+2),cellA[1])
            cellD = (ord(cellB[0]-2),cellB[1])
        else:
            cellC = (ord(cellA[0]-2),cellA[1])
            cellD = (ord(cellB[0]+3),cellB[1])
        cl.perform_castling_at(cellA, cellB, cellC, cellD)
        plycount+=1
        return ("", plycount)

    # Do en_passant
    elif(move_data["en_passant"]["en_passant"]):
        piece = ["piece"]
        rowP, colP = piece[:1], int(piece[1:])
        piece_cell = (rowP,colP)

        cellTake = move_data["en_passant"]["en_passant"]["square"]
        cl.en_passant(cellA, cellB, cellTake, piece)
        plycount+=1
        return ("", plycount)

    # Do move_piece
    else:
        cl.move_piece(cellA, cellB)
        plycount+=1
        return ("", plycount)
