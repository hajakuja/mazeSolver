from graphics import Window, Line, Point
from cell import cell
import random



def main():
    window = Window(1080, 720)
    # window.draw_line(Line(Point(100, 100), Point(350, 450)), "Red")
    cells: list[cell] = []
    for i in range(50,750, 50):
        for j in range(10, 550, 50):
            cells.append(cell(i, j, i+50, j+50, window))
    for c in cells:
        i = random.randint(1,4)
        if i == 1:
            c.has_left_wall = False
        elif i == 2:
            c.has_right_wall = False
        elif i == 3:
            c.has_bottom_wall = False
        else:
            c.has_top_wall = False
        c.draw()

    cells[2].draw_move(cells[13])
    window.wait_for_close()

if __name__ == "__main__":
    main()