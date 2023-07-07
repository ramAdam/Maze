import pdb
from utils.commons import direction


class GridRenderer:
    def __init__(self):
        self.symbols = {1: "   |", 2: "|  |",
                        3: "|__", 4: "__|", 5: " __ ", 6: "|   ", 7: "   "}
    # def draw(self, grid):
    #     self._drawNorthernTopBorder(grid.row)
    #     for i in range(0, grid.row+1):

    #         self._spaceFromStart()
    #         self._drawNorthAndSouth()

    #         for j in range(0, grid.col-1):
    #             self._drawNorthAndSouth()

    #         self._drawEndOfRow()
    #     pdb.set_trace()

    def draw(self, grid):
        self._drawNorthernTopBorder(grid.row)
        # print()
        for rdx in range(0, grid.row):
            self._spaceFromStart(10)
            for cdx in range(0, grid.col):
                # pdb.set_trace()
                self._print_cell(grid[rdx, cdx])

            print()
            # self._drawEndOfRow()
        pdb.set_trace()

    def _print_cell(self, cell):
        open = ""
        pipe = "|"

        print(cell, end='')

    def _spaceFromStart(self, nspaces=5):
        """
        spaces grid from start and draw
        starting border
        """
        space = " "
        print(10 * space, end='')

    def _drawNorthAndSouth(self, north=True, south=True):
        print("|"+"__"+"", end='')

    def _drawEndOfRow(self):
        print("|", end='')
        print()

    def _drawNorthernTopBorder(self, row):
        print()
        step = "__" + " "
        space = " "
        print(11 * space, end='')
        print(step * row)
