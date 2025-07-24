import pygame


class MenuScene:
    def __init__(self, app):
        self.app = app
        self.screen = app.screen
        self.font = pygame.font.Font(None, 48)
        self.running = True
        self.start_game = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.app.running = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.start_game = True
                self.running = False

    def update(self):
        pass  

    def draw(self, screen):
        self.screen.fill((0, 0, 0))
        text = self.font.render(
            "Appuyez sur une touche pour commencer", True, (255, 255, 255)
        )
        rect = text.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
        )
        self.screen.blit(text, rect)
