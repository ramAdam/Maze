from maze.board import Grid, Cell
from utils.commons import direction, map
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

    def test_link_nbrs(self):
        cell = Cell(1, 3)
        nbr = Cell(2, 3)
        grid = Grid(4, 4)
        grid.link(cell, nbr, "south")

    def test_get_nbrs(self):

        cell = self.grid._get_nbrs(0, 0)

        south = cell.nbrs[direction.SOUTH]
        east = cell.nbrs[direction.EAST]

        self.assertIsNone(cell.nbrs[direction.NORTH])
        self.assertIsNotNone(cell.nbrs[direction.SOUTH])

        self.assertEquals((south.row, south.col), (1, 0))

        self.assertIsNone(cell.nbrs[direction.WEST])
        self.assertIsNotNone(cell.nbrs[direction.EAST])

        self.assertEquals((east.row, east.col), (0, 1))

    def test_get_location(self):
        # mid_north = self.grid[0, 1]
        grid = self.grid

        self.assertEqual(grid.get_location(grid[0, 1]), map.MID_NORTH)
        self.assertEqual(grid.get_location(grid[0, 0]), map.NW)
        self.assertEqual(grid.get_location(grid[0, 3]), map.NE)
        self.assertEqual(grid.get_location(grid[3, 3]), map.SE)
        self.assertEqual(grid.get_location(grid[3, 0]), map.SW)

        self.assertEqual(grid.get_location(grid[2, 1]), map.MID)
        self.assertEqual(grid.get_location(grid[2, 2]), map.MID)

        self.assertEqual(grid.get_location(grid[2, 3]), map.MID_EAST)
        self.assertEqual(grid.get_location(grid[3, 1]), map.MID_SOUTH)

    def test_iterator(self):
        """
        throws a index error if the loop
        doesn't stop normally
        """

        for cell in self.grid:
            pass
