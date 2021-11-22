import unittest
from algos.bin_tree import BinaryTree
from maze.board import Grid, Cell
import pdb


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(4, 4)

    def test_grid(self):
        maze = BinaryTree.onGrid(self.grid)
        self.assertTrue(expr)(maze.path([0, 0], [0, 3]))

    def test_link(self):

        maze = BinaryTree()
        cell = self.grid[0, 1]
        maze.on(self.grid)
        pdb.set_trace()
        nbrs = maze.get_choices(cell, self.grid)

        self.assertEqual(len(nbrs), 1)
        selected_nbr = maze._choose_random_nbr(nbrs)
        maze.link(cell, selected_nbr)

        self.assertEqual(cell.nbrs["east"], selected_nbr)
        self.assertEqual(selected_nbr.nbrs["west"], cell)

    def test_choose_random_nbr(self):
        pass
