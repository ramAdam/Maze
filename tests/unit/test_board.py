from maze.board import Grid, Cell
import unittest
import pdb


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(1, 4)

    def test_next_nbr_is_none(self):
        for nbr in self.cell:
            self.assertIsNone(nbr)


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(4, 4)
        self.cell = Cell(1, 4)

    def test_get_neighbors(self):
        nbrs = self.grid.get_neighbors(self.cell)
        self.assertEqual(len(nbrs), 0)
