# app/scenes/game_scene.py
import pygame
from models.Players.joueur import Player
from .base_scene import Scene
from app.scenes.end_scene import EndScene


class GameScene:
    def __init__(self, app, grid):
        self.app = app
        self.grid = grid
        self.player = Player(grid.entree)
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_z]:
            self.player.deplacer("up", self.grid.grid, self.grid.sortie)
        elif keys[pygame.K_s]:
            self.player.deplacer("bottom", self.grid.grid, self.grid.sortie)
        elif keys[pygame.K_q]:
            self.player.deplacer("left", self.grid.grid, self.grid.sortie)
        elif keys[pygame.K_d]:
            self.player.deplacer("right", self.grid.grid, self.grid.sortie)

    def update(self):
        if self.player.has_won:
            self.running = False
            self.app.set_scene(EndScene(self.app.screen, message="Vous avez gagné !"))

    def draw(self, screen):
        screen.fill((255, 255, 255))
        for y in range(self.grid.height):
            for x in range(self.grid.width):
                rect = pygame.Rect(x * 10, y * 10, 10, 10)
                if (y, x) == self.grid.entree:
                    pygame.draw.rect(screen, (0, 255, 0), rect)
                elif (y, x) == self.grid.sortie:
                    pygame.draw.rect(screen, (255, 0, 0), rect)
                elif self.grid.grid[y][x] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), rect)
                else:
                    pygame.draw.rect(screen, (200, 200, 200), rect)

            # Dessiner la traînée du joueur

        for y, x in self.player.visited_cells:
            rect = pygame.Rect(x * 10, y * 10, 10, 10)
            pygame.draw.rect(screen, (150, 150, 255), rect)  # bleu clair

        # Dessiner le joueur par-dessus
        y, x = self.player.position
        pygame.draw.rect(
            screen, (0, 0, 255), pygame.Rect(x * 10, y * 10, 10, 10)
        )  # bleu foncé
