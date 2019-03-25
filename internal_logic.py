import json
import client as cl


# Function to select the appropriate move based on the json data (move_data)
# move_data has the form jsondata["history"][n], where n is the move identifier
def parseJson(move_data, plycount):
    print(move_data)

    if (move_data==None):
        return "Data empty"

    _from = move_data["from"]
    to = move_data["to"]

    rowA, colA = _from[:1].upper(), int(_from[1:])
    cellA = (rowA,colA)

    rowB, colB = to[:1].upper(), int(to[1:])
    cellB = (rowB,colB)

    # Do take_piece
    if(move_data["capture"]["capture"]):
        pieceA = move_data['piece']
        pieceB = move_data['capture']['piece']
        piece_str = move_data["capture"]["initial_pos_piece"]
        rowP, colP = piece_str[:1].upper(), int(piece_str[1:])
        piece_cell = (rowP,colP)

        cl.take_piece(cellA, cellB, piece_cell, pieceA, pieceB)
        plycount+=1
        return plycount

    # Do castling
    elif(move_data["castle"]["castle"]):
        if (move_data["castle"]["side"]=='k'):
            cellC = ('H',cellA[1])
            cellD = ('F',cellB[1])
        else:
            cellC = ('A',cellA[1])
            cellD = ('D',cellB[1])

        pieceA = 'k'
        pieceB = 'r'
        cl.perform_castling_at(cellA, cellC, cellB, cellD, pieceA, pieceB)
        plycount+=1
        return plycount

    # Do en_passant
    elif(move_data["en_passant"]["en_passant"]):
        piece = move_data["en_passant"]["initial_pos_piece"]
        rowP, colP = piece[:1].upper(), int(piece[1:])
        piece_cell = (rowP,colP)


        cellTake = move_data["en_passant"]["square"]
        cl.en_passant(cellA, cellB, cellTake, piece_cell)
        plycount+=1
        return plycount

    # Do move_piece
    else:
        piece = move_data['piece']
        cl.move_piece(cellA, cellB, piece)
        plycount+=1
        return plycount
