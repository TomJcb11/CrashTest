import random

from models.Grids.abc_grid import Grid


class DFSGrid(Grid):
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
        # self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        visited = [[False for _ in range(self.width)] for _ in range(self.height)]

        def dfs(y, x):
            visited[y][x] = True
            self.grid[y][x] = 0
            directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(directions)

            for dy, dx in directions:
                ny, nx = y + dy, x + dx
                if 0 < ny < self.height and 0 < nx < self.width and not visited[ny][nx]:
                    wall_y, wall_x = y + dy // 2, x + dx // 2
                    self.grid[wall_y][wall_x] = 0
                    dfs(ny, nx)

        # point de départ forcé sur une cellule impaire pour assurer les murs entre
        start_y = self.entree[0] if self.entree[0] % 2 == 1 else self.entree[0] + 1
        start_x = self.entree[1] if self.entree[1] % 2 == 1 else self.entree[1] + 1

        dfs(start_y, start_x)

        # Define the exit point of the maze
        possible_exits = [
            (self.height - 1, x)
            for x in range(1, self.width - 1)
            if self.grid[self.height - 1][x] == 0
        ]
        if possible_exits:
            self.sortie = random.choice(possible_exits)  # noqa: S311
        else:
            # Si aucune sortie valide, on en crée une en forçant une ouverture
            fallback_x = random.choice(range(1, self.width - 1, 2))  # noqa: S311
            self.sortie = (self.height - 1, fallback_x)
            self.grid[self.sortie[0]][self.sortie[1]] = 0
