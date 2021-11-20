class Grid:
    def __init__(self, width, height):
        pass

    def get_neighbors(self, cell):
        """
        returns all list of all neighboring cells
        """
        return [nbr for nbr in cell if nbr]


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.nbrs = {"north": None, "south": None, "east": None, "west": None}

    def __iter__(self):
        return iter(self.nbrs.values())
