import random


class BinaryTree:

    def on(self, grid):
        for cell in grid:
            nbrs = grid.get_neighbors(cell)
            choosen_nbr = self._choose_random_nbr(nbrs)
            grid.link(cell, choosen_nbr)

        return grid.maze()

    def _choose_random_nbr(self, neighbors):
        """
        neighbors is a list of cells
        returns a random neighbor from the list
        """

        index = random.choice(range(0, len(neighbors)))
        return neighbors[index]
