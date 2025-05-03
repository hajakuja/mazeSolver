from cell import Cell
from graphics import Window, Point, Line
import time
import random
class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win:Window = None,
        seed = None, 
        sleep = 0.05
    ):
        self.x1 = x1
        self.y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: list[list[Cell]] = []
        self.__seed = seed
        self.__sleep = sleep
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self.x1 + i * self._cell_size_x
        y1 = self.y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(self.__sleep)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        if self.__seed is not None:
            random.seed(self.__seed)
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i-1][j].visited:
                    to_visit.append((i-1, j))
            if i < self._num_cols-1 and  not self._cells[i+1][j].visited:
                    to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                    to_visit.append((i, j-1))
            if j < self._num_rows-1 and not self._cells[i][j+1].visited:
                    to_visit.append((i, j+1))
                    
            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return 
            direction = to_visit[random.randrange(len(to_visit))]
            if direction[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if direction[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if direction[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if direction[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            self._break_walls_r(*direction)
    
    def _reset_cells_visited(self):
        for i in self._cells:
             for c in i:
                  c.visited = False
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self, i, j):
        
        self._animate()
        self._cells[i][j].visited = True
        
        if i == self._num_cols-1 and j == self._num_rows -1:
             return True
        #left        
        if i > 0 and not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            ret = self._solve_r(i-1,j)
            if ret:
                 return ret
            else:
                 self._cells[i][j].draw_move(self._cells[i-1][j], True)
        #right
        if i < self._num_cols-1 and  not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            ret = self._solve_r(i+1,j)
            if ret:
                 return ret
            else:
                 self._cells[i][j].draw_move(self._cells[i+1][j], True)
        #top    
        if j > 0 and not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            ret = self._solve_r(i,j-1)
            if ret:
                 return ret
            else:
                 self._cells[i][j].draw_move(self._cells[i][j-1], True)
        #bottom
        if j < self._num_rows-1 and not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            ret = self._solve_r(i,j+1)
            if ret:
                 return ret
            else:
                 self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False