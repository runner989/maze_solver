import unittest
import time
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
        time.sleep(60)
        m2 = Maze(50, 50, 8, 8, 20, 20, win)
        self.assertEqual(
            len(m2._cells),
            num_cols
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows
        )
        time.sleep(60)
        m3 = Maze(10, 10, num_rows*2, num_cols*2, 5, 10, win)
        self.assertEqual(
            len(m3._cells),
            num_cols
        )
        self.assertEqual(
            len(m3._cells[0]),
            num_rows
        )
        time.sleep(60)

if __name__ == "__main__":
    unittest.main()
