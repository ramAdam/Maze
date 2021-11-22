import pdb
from utils.commons import direction, map


class Grid:
    def __init__(self, row, col):
        self.north = None
        self.east = None
        self.row = row
        self.col = col
        self.grid = self._create_grid(self.row, self.col)

    def _create_grid(self, row, col):
        if row < 3 and col < 3:
            raise ValueError(
                "row and col has to be greater than or equal to 3")
        rows = list()
        cols = list()

        for r_idx in range(0, row):
            for c_idx in range(0, col):
                cols.append(Cell(r_idx, c_idx))
            rows.append(list(cols))
            cols.clear()
        self._set_north(rows)
        self._set_east(rows)
        return rows

    def _set_north(self, grid):
        self.north = grid[0]

    def _set_east(self, grid):
        self.east = list()

        for idx in range(0, len(grid)):
            self.east.append(grid[idx][self.col-1])

    def get_neighbors(self, cell):
        """
        returns list of all neighboring cells
        """
        return [nbr for nbr in cell if nbr]

    def cell_in_cornor(self, dir, cell):
        """
        returns true if the cell is in direction
        otherwise false
        """
        if dir == direction.NORTH:
            return self._sides_contains(cell, self.north)
        elif dir == direction.EAST:
            return self._sides_contains(cell, self.east)

    def _sides_contains(self, cell, side):
        for sel in side:
            if sel == cell:
                return True
        return False

    def __getitem__(self, idxtup):
        row, col = idxtup

        if row < 0 or col < 0:
            raise IndexError
        return self.grid[row][col]

    def get_location(self, cell):
        # row, col = (cell.row, cell.col)
        IS_FIRST_ROW = (cell.row == 0)
        IS_LAST_ROW = (cell.row == self.row-1)
        IS_FIRST_COL = (cell.col == 0)
        IS_LAST_COL = (cell.col == self.col-1)

        IS_MID_ROW = (cell.row > 0 and (cell.row < self.row-1))
        IS_MID_COL = (cell.col > 0 and (cell.col < self.col-1))

        IS_NW_COR = (IS_FIRST_ROW and IS_FIRST_COL)
        IS_NE_COR = (IS_FIRST_ROW and IS_LAST_COL)
        IS_SW_COR = (IS_LAST_ROW and IS_FIRST_COL)
        IS_SE_COR = (IS_LAST_ROW and IS_LAST_COL)

        IS_MID_NORTH = IS_MID_COL and IS_FIRST_ROW
        IS_MID_WEST = IS_FIRST_COL and IS_MID_ROW
        IS_MID_EAST = IS_LAST_COL and IS_MID_ROW
        IS_MID_SOUTH = IS_LAST_ROW and IS_MID_COL

        if IS_NW_COR:
            return map.NW
        elif IS_NE_COR:
            return map.NE
        elif IS_SE_COR:
            return map.SE
        elif IS_SW_COR:
            return map.SW
        elif IS_MID_NORTH:
            return map.MID_NORTH
        elif IS_MID_SOUTH:
            return map.MID_SOUTH
        elif IS_MID_EAST:
            return map.MID_EAST
        elif IS_MID_WEST:
            return map.MID_WEST
        else:
            return map.MID

    def _get_nbrs(self, row, col):

        ABOVE = (row-1, col)
        BELOW = (row+1, col)
        RIGHT = (row, col+1)
        LEFT = (row, col-1)

        sides = [ABOVE, BELOW, RIGHT, LEFT]
        for dir, idx in zip(direction._asdict().values(), sides):
            try:
                self[row, col].nbrs[dir] = self[idx]
            except IndexError:
                self[row, col].nbrs[dir] = None

        return self[row, col].nbrs

    def __iter__(self):
        return GridIterator(self)


class GridIterator:
    def __init__(self, grid):
        self.grid = grid
        self.row = 0
        self.col = 0

    def __next__(self):
        self._inc_before()
        cell = self.grid[self._get_row(), self.col]
        self._inc_after()
        return cell

    def _inc_after(self):
        if self.col < self.grid.col:
            self.col += 1

    def _inc_before(self):
        if self.col >= self.grid.col:
            self.col = 0
            self.row += 1

    def _get_row(self):
        if self.row >= self.grid.row:
            raise StopIteration
        else:
            return self.row


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.nbrs = {"north": None, "south": None, "east": None, "west": None}

    def __iter__(self):
        return iter(self.nbrs.values())

    def __repr__(self):
        return f"Cell(row={self.row}, col={self.col})"

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
