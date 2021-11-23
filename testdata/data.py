from maze.board import Cell
from utils.commons import direction, map

cell_with_all_nbrs_set = Cell(2, 2)
north = Cell(1, 2)
south = Cell(2, 3)
east = Cell(3, 2)
west = Cell(2, 1)
nbrs = {direction.NORTH: north, direction.SOUTH: south,
        direction.EAST: east, direction.WEST: west}
cell_with_all_nbrs_set.nbrs = nbrs
