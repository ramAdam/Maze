from maze.board import Grid, Cell
from utils.commons import direction, map
from testdata.data import *
import unittest
import pdb


class TestCell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(1, 4)

    def test_next_nbr_is_none(self):
        for nbr in self.cell:
            self.assertIsNone(nbr)

    def test_repr(self):
        cell_1 = Cell(2, 2)
        north = Cell(1, 2)
        south = Cell(3, 2)
        east = Cell(2, 3)
        west = Cell(2, 1)

        cell_1.nbrs = {direction.NORTH: north, direction.SOUTH: south,
                       direction.EAST: east, direction.WEST: west}

        self.assertEqual(cell_1.__str__(), "|__|")

        cell_2 = cell_with_west_east
        self.assertEqual(cell_2.__str__(), "|  |")

        cell_3 = cell_with_south_side
        self.assertEqual(cell_3.__str__(), " __ ")


class TestGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(4, 4)
        self.cell = Cell(1, 4)

    def test_link_nbrs(self):
        """
        should disconnect all connections
        in a cell except the desired link
        """

        self.grid.link(cell_with_all_nbrs_set, direction.EAST)

        for dir in direction:
            if dir == direction.EAST:
                self.assertEqual(cell_with_all_nbrs_set.nbrs[dir], east)
            else:
                self.assertIsNone(cell_with_all_nbrs_set.nbrs[dir])

    def test_get_nbrs(self):

        nbrs = self.grid._get_nbrs(0, 0)
        south = nbrs[direction.SOUTH]
        east = nbrs[direction.EAST]

        self.assertIsNone(nbrs[direction.NORTH])
        self.assertIsNotNone(nbrs[direction.SOUTH])

        self.assertEqual((south.row, south.col), (1, 0))

        self.assertIsNone(nbrs[direction.WEST])
        self.assertIsNotNone(nbrs[direction.EAST])

        self.assertEqual((east.row, east.col), (0, 1))

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
