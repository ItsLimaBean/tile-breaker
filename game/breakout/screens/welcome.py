import pygame
from screens import BaseScreen
from components import TextBox


class WelcomeScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.welcometext = TextBox((300, 100), "WELCOME GAMERS", color=(0, 0, 0), bgcolor=(255, 255, 255))
        self.button = TextBox(
            (400, 100), "Press SPACE", color=(255, 255, 255), bgcolor=(0, 0, 0)
        )
        self.sprites.add(self.button)
        self.sprites.add(self.welcometext)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.button.rect.x = 200
        self.button.rect.y = 400
        self.welcometext.rect.x = 200
        self.welcometext.rect.y = 200
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        print(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            self.next_screen = "game"
            self.running = False
