import random
import pdb
from utils.commons import direction, map


class BinaryTree:

    def on(self, grid):
        for cell in grid:
            nbrs = self.get_choices(cell, grid)
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

    def get_choices(self, cell, grid):
        """
        returns a list of cell with direction
        """
        # grd = grid.grid
        all_nbrs = grid._get_nbrs(cell.row, cell.col)
        loc = grid.get_location(cell)

        all_dirs = [direction.NORTH, direction.SOUTH,
                    direction.EAST, direction.WEST]

        if loc == map.MID_EAST:
            return self._set_directions(cell, [direction.SOUTH], all_nbrs)

        elif loc == map.NE:
            return self._set_directions(
                cell, [direction.SOUTH, direction.WEST], all_nbrs)
        elif loc == map.SE:
            return self._set_directions(
                cell, [direction.NORTH, direction.WEST], all_nbrs)
        elif loc == map.NW:
            return self._set_directions(cell, [direction.EAST], all_nbrs)
        elif loc == map.MID_NORTH:
            return self._set_directions(cell, [direction.EAST], all_nbrs)
        else:
            return self._set_directions(cell, all_dirs, all_nbrs)

    def _set_directions(self, cell, dirs, nbrs):
        for dir in direction._asdict().values():
            if dir not in all_dirs:
                cell.nbrs[dir] == None

        return cell.nbrs
