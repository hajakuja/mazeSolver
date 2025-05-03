from graphics import Window
# from cell import cell
from maze import Maze
import random
import sys


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) // num_cols
    cell_size_y = (screen_y - 2 * margin) // num_rows
    win = Window(screen_x, screen_y)
    if len(sys.argv) > 1:
        print(sys.argv[1])
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, sleep=float(sys.argv[1]))
    else:
        maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()
    
if __name__ == "__main__":
    main()