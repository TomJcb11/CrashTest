import pygame


class EndScene:
    def __init__(self, screen, message="Vous avez gagné !"):
        self.screen = screen
        self.message = message
        self.font = pygame.font.Font(None, 48)
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.running = False

    def update(self):
        # On ne met rien ici si tout est géré dans handle_events
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))  # fond noir
        text_surface = self.font.render(self.message, True, (0, 255, 0))
        rect = text_surface.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2)
        )
        screen.blit(text_surface, rect)
