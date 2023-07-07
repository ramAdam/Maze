import unittest
from maze.board import Grid
from render.renderer import GridRenderer
from algos.bin_tree import BinaryTree
import pdb


class TestRenderer(unittest.TestCase):
    def setUp(self):
        self.grd_rendr = GridRenderer()
        self.grid = Grid(4, 4)
        bin_t = BinaryTree()
        bin_t.on(self.grid)

    def test_draw(self):
        """
        renders the grid
        """
        self.grd_rendr.draw(self.grid)
