import unittest
from maze import Maze
from graphics import Window

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.win = Window(800, 600)
        self.maze = Maze(50, 50, 5, 5, 50, 50, self.win)
        self.win.wait_for_close()
        
    def test_break_entrance_and_exit(self):
        # Check entrance
        self.assertFalse(self.maze._cells[0][0].has_top_wall, "Entrance top wall should be removed")
        
        # Check exit
        self.assertFalse(self.maze._cells[self.maze._num_cols - 1][self.maze._num_rows - 1].has_bottom_wall, "Exit bottom wall should be removed")

if __name__ == "__main__":
    unittest.main()
