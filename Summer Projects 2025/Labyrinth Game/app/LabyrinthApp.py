# app/app.py
import pygame


class LabyrinthApp:
    def __init__(self, window_size):
        pygame.init()
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Visualisation Labyrinthe")
        self.clock = pygame.time.Clock()
        self.scene = None
        self.running = True

    def set_scene(self, scene):
        self.scene = scene

    def run(self):
        while self.running and self.scene and self.scene.running:
            self.scene.handle_events()
            self.scene.update()
            self.scene.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
