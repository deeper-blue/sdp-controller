# Test script that sends all available commands in a sequence.
# Intended to be used with a dummy HLI on the other side.
#
# Author(s):
#   Filip Smola

import client as c

c.reset()
input("Waiting for Enter...")

c.move_piece(('E',2),('E',4))
input("Waiting for Enter...")

c.move(('A',1),('L',8))
input("Waiting for Enter...")

c.take_piece(('E',4),('D',5),('D',7))
input("Waiting for Enter...")

c.perform_castling_at(('E',1),('C',1),('A',1),('D',1))
input("Waiting for Enter...")

c.en_passant(('E',4),('D',5),('D',4),('D',7))
