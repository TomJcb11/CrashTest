from models.Grids.abc_grid import Grid


class SimpleGrid(Grid):
    def __init__(
        self,
        width,
        height,
    ):
        super().__init__(
            width,
            height,
        )

    def _carve_path(self):
        """Carve a simple path from the entrance to the exit.

        This implementation creates a direct L-shaped path by moving horizontally
        toward the exit's x-coordinate, then vertically down toward the exit's y-coordinate.
        """
        y, x = self.entree
        self.grid[y][x] = 0
        while (y, x) != self.sortie:
            if x != self.sortie[1]:
                x += 1 if x < self.sortie[1] else -1
            elif y < self.sortie[0]:
                y += 1
            self.grid[y][x] = 0
