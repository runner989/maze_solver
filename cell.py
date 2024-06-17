from graphics import Line, Point

class Cell():
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self._win is None:
            return
        x1 = self._x1
        y1 = self._y1
        x2 = self._x2
        y2 = self._y2
        fill_color = "black"
        background_color = "#d9d9d9"

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, background_color)

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, background_color)

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, background_color)

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, background_color)


    def draw_move(self, to_cell, undo=False):
        if undo:
            color = "gray"
        else:
            color = "red"
            
        x1 = (self._x1 + self._x2) // 2
        y1 = (self._y1 + self._y2) // 2
        x2 = (to_cell._x1 + to_cell._x2) // 2
        y2 = (to_cell._y1 + to_cell._y2) // 2
        line = Line(Point(x1, y1), Point(x2, y2))       
        self._win.draw_line(line, fill_color=color)
