import matplotlib.pyplot as plt
import numpy as np
import chess as chess
import plot as plot


start_position = (3,4)
my_board = chess.chessBoard(size = 8, start_pos=start_position)
my_board.run()
plot.plot(my_board)