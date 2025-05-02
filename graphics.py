from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze"
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)


class Point():
    def __init__(self, x = 0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, a:Point, b:Point):
        self.a = a
        self.b = b

    def draw(self, canvas:Canvas, fill_color:"black"):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color , width=2)