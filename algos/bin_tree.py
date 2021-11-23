import random
import pdb
from utils.commons import direction, map


class BinaryTree:

    def on(self, grid):
        for cell in grid:
            nbrs = self.get_choices(cell, grid)
            choosen_nbr = self._choose_random_nbr(nbrs)
            grid.link(cell, choosen_nbr)

        # return grid.maze()

    def _choose_random_nbr(self, neighbors):
        """
        neighbors is dictionary of direction mapped to cells
        returns - a random direction key
        """
        if not neighbors:
            return None
        lkeys = list(neighbors.keys())
        index = random.choice(range(0, len(lkeys)))
        chosen_key = lkeys[index]
        return chosen_key

    def get_choices(self, cell, grid):
        """
        returns a list of dictionary of all choices available
        """
        # south east will have no choice, special case
        # grd = grid.grid
        all_nbrs = grid._get_nbrs(cell.row, cell.col)
        loc = grid.get_location(cell)

        # if cell.row == 1 and cell.col == 0:
        #     pdb.set_trace()

        all_dirs = [direction.NORTH, direction.EAST]

        if loc == map.MID_EAST or loc == map.NE:
            return self._set_directions(cell, [direction.SOUTH], all_nbrs)
        elif loc == map.NW or loc == map.MID_NORTH:
            return self._set_directions(cell, [direction.EAST], all_nbrs)
        elif loc == map.SE:
            return self._set_directions(cell, [], all_nbrs)

        else:
            return self._set_directions(cell, all_dirs, all_nbrs)

    def _set_directions(self, cell, dirs, nbrs):
        """
        sets permissible directions of a cell
        as per binary tree algo
        """
        # if len(dirs) == 0:
        #     return None

        for dir in direction:
            if dir not in dirs:
                cell.nbrs[dir] = None

        return {dir: cell for dir, cell in cell.nbrs.items() if cell}
