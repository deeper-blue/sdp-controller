#!/usr/bin/env python3
# The major functions of client are converting given command into a separatable string
# and send the string to the server(ev3)
# Author(s):
#   Wanjing Chen

import socket

HOST = '192.168.105.116'  # The server's hostname or IP address
# HOST = "127.0.0.1"
PORT = 64432        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# The following several functions are to convert the given commands into a later seperatable string
def move_piece(cellA,cellB):
    message = 'move_piece;' + str(cellA) + ';' + str(cellB)
    print("Sent: %s" % (send(message)))

def move(cellA, cellB):
    message = 'move;' + str(cellA) + ';' + str(cellB)
    print("Sent: %s" % (send(message)))

def take_piece(cellA, cellB, piece):
    message = 'take_piece;' + str(cellA) + ';' + str(cellB) + ';' + str(piece)
    print("Sent: %s" % (send(message)))

def perform_castling_at(cellA, cellB, cellC, cellD):
    message = 'perform_castling_at;' + str(cellA) + ';' + str(cellB) + ';' + str(cellC) + ';' + str(cellD)
    print("Sent: %s" % (send(message)))

def reset():
    message = 'reset;'
    print("Sent: %s" % (send(message)))

# This function is to send the message to the server(ev3)
def send(message):
    s.sendall(str.encode(message))
    return s.recv(1024)


move_piece(('A',1),('A',2))
#print('Received', repr(data))
take_piece(('A',3),('A',4),'black_queen')
