import pygame
import time

from models.Grids.simple_grid import SimpleGrid
from models.Grids.dfs_grid import DFSGrid
from models.Players.joueur import Player

CELL_SIZE = 10
WIDTH = 50
HEIGHT = 50
WINDOW_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)

COLOR_WALL = (0, 0, 0)  # Black for walls
COLOR_EMPTY = (255, 255, 255)  # White for empty spaces
COLOR_PATH = (200, 200, 200)  # Light gray for paths
# Colors for start and end points
COLOR_START = (0, 255, 0)
COLOR_END = (255, 0, 0)
# Color for player
COLOR_PLAYER = (0, 0, 255)


def run_app():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Visualisation Labyrinthe")

    # grid = SimpleGrid(WIDTH, HEIGHT)
    grid = DFSGrid(WIDTH, HEIGHT)

    player = Player(grid.entree)
    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player movement handling
        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            player.deplacer("up", grid.grid, grid.sortie)
        elif keys[pygame.K_s]:
            player.deplacer("bottom", grid.grid, grid.sortie)
        elif keys[pygame.K_q]:
            player.deplacer("left", grid.grid, grid.sortie)
        elif keys[pygame.K_d]:
            player.deplacer("right", grid.grid, grid.sortie)

        # draw the map
        for y in range(grid.height):
            for x in range(grid.width):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if (y, x) == grid.entree:
                    pygame.draw.rect(screen, COLOR_START, rect)
                elif (y, x) == grid.sortie:
                    pygame.draw.rect(screen, COLOR_END, rect)
                elif grid.grid[y][x] == 1:
                    pygame.draw.rect(screen, COLOR_WALL, rect)
                else:
                    pygame.draw.rect(screen, COLOR_PATH, rect)

        # draw the player
        y, x = player.position
        player_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, COLOR_PLAYER, player_rect)

        if player.has_won:
            font = pygame.font.Font(None, 36)
            text = font.render("Vous avez gagné !", True, (0, 255, 0))
            screen.blit(text, (10, 10))
            running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
