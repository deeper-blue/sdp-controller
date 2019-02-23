#!/usr/bin/env python3

import socket

HOST = '192.168.105.116'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def move_piece(cellA,cellB):
    message = 'move_piece;' + str(cellA) + ';' + str(cellB) + ';'
    print("Received: %s" % (send(message)))

def move(cellA, cellB):
    message = 'move;' + str(cellA) + ';' + str(cellB) + ';'
    print("Received: %s" % (send(message)))

def take_piece(cellA, cellB, piece):
    message = 'take_piece;' + str(cellA) + ';' + str(cellB) + ';' + str(piece) + ';'
    print("Received: %s" % (send(message)))

def perform_castling_at(cellA, cellB, cellC, cellD):
    message = 'perform_castling_at;' + str(cellA) + ';' + str(cellB) + ';' + str(cellC) + ';' + str(cellD) + ';'
    print("Received: %s" % (send(message)))

def reset():
    message = 'reset;'
    print("Received: %s" % (send(message)))

def send(message):
    s.sendall(str.encode(message))
    return s.recv(1024)

move_piece(('A',1),('A',2))
#print('Received', repr(data))
take_piece(('A',3),('A',4),'queen')
