from graphics import Window, Line, Point
class Cell():
    def __init__(self, window:Window, x1=None, y1=None, x2=None, y2=None, 
                 left_wall = True, right_wall=True,
                 top_wall = True, bottom_wall = True):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = window
        self.has_left_wall = left_wall
        self.has_right_wall = right_wall
        self.has_top_wall = top_wall
        self.has_bottom_wall = bottom_wall
        self.visited = False
    
    def draw(self, x1=None, y1=None, x2=None, y2=None):
        if x1:
            self.__x1 = x1
        if x2:
            self.__x2 = x2
        if y1:
            self.__y1 = y1
        if y2:
            self.__y2 = y2
        color = {False:"White", True:"Black"}
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x1, self.__y2)
        self.__win.draw_line(Line(p1,p2), color[self.has_left_wall])
        p1 = Point(self.__x2, self.__y1)
        p2 = Point(self.__x2, self.__y2)
        self.__win.draw_line(Line(p1,p2), color[self.has_right_wall])
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x2, self.__y1)
        self.__win.draw_line(Line(p1,p2), color[self.has_top_wall])
        p1 = Point(self.__x1, self.__y2)
        p2 = Point(self.__x2, self.__y2)
        self.__win.draw_line(Line(p1,p2), color[self.has_bottom_wall])
    
    
    def draw_move(self, to_cell, undo=False):
        color = {False:"Red", True:"light grey"}
        half_length = abs(self.__x2 - self.__x1)//2
        p1 = Point(half_length + self.__x1, half_length + self.__y1)
        half_length2 = abs(to_cell.__x1 - to_cell.__x2)//2 
        p2 = Point(half_length2 + to_cell.__x1, half_length2 + to_cell.__y1)
        self.__win.draw_line(Line(p1, p2), color[undo])