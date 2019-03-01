# Script for Demo 2 demonstration.
# Resets, waits for Enter and moves a piece from E2 to E4.
#
# Author(s):
#   Filip Smola

import client as c

c.reset()
input("Waiting for Enter...")
c.move_piece(('E',2),('E',4))
