from collections import deque


class Player:
    """Represent a player in the labyrinth game.

    Attributes:
        position (tuple[int, int]): Current position of the player in the grid.

    """

    def __init__(self, position_initiale):
        """Initialise le joueur à la position donnée.

        Args:
            position_initiale (tuple[int, int]): Coordonnées (y, x) de départ.

        """
        self.position = position_initiale
        self.has_won = False
        self.visited_cells = deque(
            maxlen=5
        )  # fifo queue to keep track of last 5 visited cells
        self.visited_cells.append(self.position)

    def deplacer(self, direction, grid, exit):
        """Déplace le joueur dans la direction indiquée si la case est libre.

        Args:
            direction (str): 'haut', 'bas', 'gauche', 'droite'
            grid (list[list[int]]): grid du labyrinthe (0 = vide, 1 = mur)
            exit (tuple[int, int]): Position de la sortie du labyrinthe

        """
        y, x = self.position
        if direction == "up":
            nouvelle_pos = (y - 1, x)
        elif direction == "bottom":
            nouvelle_pos = (y + 1, x)
        elif direction == "left":
            nouvelle_pos = (y, x - 1)
        elif direction == "right":
            nouvelle_pos = (y, x + 1)
        else:
            return  # invalid direction

        self.visited_cells.append(
            self.position
        )  # Add current position to visited cells

        # Vérifie si nouvelle position valide
        ny, nx = nouvelle_pos
        if (
            0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 0
        ):  # if target between x and y boundaries and if destination is not wall :
            self.position = nouvelle_pos
            self.has_won = self.position == exit
