# app/main.py
from app.LabyrinthApp import LabyrinthApp
from app.scenes.game_scene import GameScene
from models.Grids.dfs_grid import DFSGrid
from models.Grids.simple_grid import SimpleGrid

WIDTH, HEIGHT = 50, 50
CELL_SIZE = 10
WINDOW_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)


def main():
    app = LabyrinthApp(WINDOW_SIZE)
    grid_type = input("Choose grid type (simple/dfs): ").strip().lower()
    grid = DFSGrid(WIDTH, HEIGHT) if grid_type == "dfs" else SimpleGrid(WIDTH, HEIGHT)
    app.set_scene(GameScene(app, grid))
    app.run()


if __name__ == "__main__":
    main()
