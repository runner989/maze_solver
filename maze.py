from cell import Cell
import random
import time


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                x1 = self._x1 + i * self._cell_size_x
                y1 = self._y1 + j * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2, self._win)
                column.append(cell)
            self._cells.append(column)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        while True:
            next_index_list = []

            # # determine which cell(s) to visit next
            # # left
            # if i > 0 and not self._cells[i - 1][j].visited:
            #     next_index_list.append((i - 1, j))
            # # right
            # if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
            #     next_index_list.append((i + 1, j))
            # # up
            # if j > 0 and not self._cells[i][j - 1].visited:
            #     next_index_list.append((i, j - 1))
            # # down
            # if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
            #     next_index_list.append((i, j + 1))


            if i > 0 and not self._cells[i - 1][j].visited and not self._cells[i][j].has_left_wall:
                next_index_list.append((i - 1, j))

            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right_wall:
                next_index_list.append((i + 1, j))

            if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top_wall:
                next_index_list.append((i, j - 1))

            if j < self._num_rows - 1  and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom_wall:
                next_index_list.append((i, j + 1))

            if len(next_index_list) == 0:
                return False
            
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            self._cells[i][j].draw_move(self._cells[next_index[0]][next_index[1]])
            if self._solve_r(next_index[0], next_index[1]):
                return True
            
            self._cells[i][j].draw_move(self._cells[next_index[0]][next_index[1]], undo=True)
        
        return False

    def solve(self):
        self._reset_cells_visited()
        if self._solve_r(0, 0):
            print("Maze solved!")
        else:
            print("Maze not solved.")