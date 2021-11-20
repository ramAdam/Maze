import unittest
from algos.bin_tree import BinaryTree
from maze.board import Grid


class TestBinaryTree(unittest.TestCase):

    def setUp(self):
        self.grid = Grid(4, 4)

    def test_integration_demo(self):
        maze = BinaryTree.onGrid(self.grid)
        self.assertTrue(expr)(maze.path([0, 0], [0, 3]))
