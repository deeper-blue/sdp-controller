#!/usr/bin/env python3
# The major functions of client are converting given command into a separatable string
# and send the string to the server(ev3)
# Author(s):
#   Wanjing Chen

import socket
import time
from controller_config import config
import sys

# Arguably dangerous to assume these exist, but OK to crash if they don't
# since these values are necessary
if len(sys.argv)>1:
    HOST = sys.argv[2]
else:
    HOST = config['robot']['ip']
    
PORT = config['robot']['port']

# Socket for connecting to robot
s = None

# Whether the connection is open
conn_open = False

# Open connection
def open():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        conn_open = True
    except Exception as exception:
        conn_open = False
        print("Connection failed: {}".format(exception))

# Close connection once done
def close():
    s.close()
    conn_open = False

# The following several functions are to convert the given commands into a later seperatable string
def move_piece(cellA,cellB):
    message = 'move_piece;' + str(cellA) + ';' + str(cellB)
    send(message)

def move(cellA, cellB):
    message = 'move;' + str(cellA) + ';' + str(cellB)
    send(message)

def take_piece(cellA, cellB, piece):
    message = 'take_piece;' + str(cellA) + ';' + str(cellB) + ';' + str(piece)
    send(message)

def perform_castling_at(cellA, cellB, cellC, cellD):
    message = 'perform_castling_at;' + str(cellA) + ';' + str(cellB) + ';' + str(cellC) + ';' + str(cellD)
    send(message)

def en_passant(cellA, cellB, cellTake, piece):
    message = 'en_passant;' + str(cellA) + ';' + str(cellB) + ';' + str(cellTake) + ';' + str(piece)
    send(message)

def reset():
    message = 'reset;'
    send(message)

# This function is to send the message to the server(ev3)
def send(message):
    t0 = time.time()
    print('Will send ' + message)
    s.sendall(str.encode(message))
    data = s.recv(4000)
    print('Received', repr(data))
    t1 = time.time()
    print("Took: %f s" % (t1 - t0))
    print("\n")
    return data
