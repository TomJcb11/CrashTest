import random
from abc import ABC, abstractmethod


class Grid(ABC):
    """A base class for creating a grid-based labyrinth.

    Attributes:
        width (int): The width of the grid.
        height (int): The height of the grid.
        grid (list): A 2D list representing the grid, initialized with 1s.
        entree (tuple): The entry point in the grid, defined as a tuple (row, column).
        sortie (tuple): The exit point in the grid, defined as a tuple (row, column).

    """

    def __init__(self, width=50, height=50):
        """Initialize the grid with all cells set to 1 (walls) and randomly place
        the entry and exit points in the first and last rows, respectively.

        This constructor sets up a grid filled with walls (1) and assigns random
        positions for the entrance and exit on the top and bottom rows.

        Args:
            largeur (int): The width of the grid. Defaults to 50.
            height (int): The height of the grid. Defaults to 50.

        """  # noqa: D205
        self.width = width
        self.height = height
        self.grid = [
            [1 for _ in range(width)] for _ in range(height)
        ]  # Using _ as loop variable means we wont use it
        self.entree = (
            1,
            random.randint(0, width - 1),  # noqa: S311
        )  # Random entry point in the first row
        self.sortie = (
            height - 1,
            random.randint(0, width - 1),  # noqa: S311
        )  # Random exit point in the last row
        self._carve_path()

    @abstractmethod
    def _carve_path(self):
        """Abstract method to carve a path in the grid.

        This method must be implemented by any subclass to define
        how the maze path is created.
        """
        pass
