import chess as chess
import plot as plot

def main():
    start_x = int(input("Starting x-position:"))
    start_y = int(input("Starting y-position:"))
    start_position = (start_x, start_y)

    my_board = chess.ChessBoard(size = 8, start_pos=start_position)
    my_board.run()
    plot.plot(my_board)

if __name__ == '__main__':
    main()