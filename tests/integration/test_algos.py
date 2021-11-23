# import unittest
# from algos.bin_tree import BinaryTree
# from maze.board import Grid, Cell
# from testdata.data import *
# import pdb


# class TestBinaryTree(unittest.TestCase):

#     def setUp(self):
#         self.grid = Grid(4, 4)

#     def test_grid(self):
#         bin_t = BinaryTree()
#         bin_t.on(self.grid)

#         self.assertAllNbrsAreNone(self.grid[3, 3].nbrs)

#     def test_choose_random_nbr(self):
#         """
#         should randomly choose between north and south
#         """
#         bin_t = BinaryTree()
#         chosen_nbr = bin_t._choose_random_nbr(
#             bin_t.get_choices(cell_with_all_nbrs_set, self.grid))

#         self.assertTrue(chosen_nbr in [direction.NORTH, direction.SOUTH])

#     def test_get_choices(self):
#         """
#         should return a list of available choices
#         """
#         bin_t = BinaryTree()
#         choices = bin_t.get_choices(cell_with_all_nbrs_set, self.grid)

#         self.assertEqual(len(choices), 2)

#     def assertAllNbrsAreNone(self, nbrs):
#         """
#         assert all neighbours are non
#         """
#         for dir in direction:
#             self.assertIsNone(nbrs[dir])
