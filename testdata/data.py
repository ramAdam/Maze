from maze.board import Cell
from utils.commons import direction, map

cell_with_all_nbrs_set = Cell(2, 2)
north = Cell(1, 2)
south = Cell(3, 2)
east = Cell(2, 3)
west = Cell(2, 1)

cell_with_all_nbrs_set.nbrs = {direction.NORTH: north, direction.SOUTH: south,
                               direction.EAST: east, direction.WEST: west}

cell_with_west_east = Cell(2, 2)
cell_with_west_east.nbrs = {direction.NORTH: None,
                            direction.SOUTH: None, direction.EAST: east, direction.WEST: west}

cell_with_south_side = Cell(2, 2)
cell_with_south_side.nbrs = {direction.NORTH: None,
                             direction.SOUTH: south, direction.EAST: None, direction.WEST: None}
