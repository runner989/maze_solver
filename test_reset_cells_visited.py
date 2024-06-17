import unittest
from graphics import Window
from maze import Maze

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.win = Window(800, 600)
        self.maze = Maze(50, 50, 5, 5, 50, 50, self.win, seed=0)

    def test_reset_cells_visited(self):
        for i in range(self.maze._num_cols):
            for j in range(self.maze._num_rows):
                self.assertTrue(self.maze._cells[i][j].visited)

        self.maze._reset_cells_visited()

        for i in range(self.maze._num_cols):
            for j in range(self.maze._num_rows):
                self.assertFalse(self.maze._cells[i][j].visited)

if __name__ == "__main__":
    unittest.main()