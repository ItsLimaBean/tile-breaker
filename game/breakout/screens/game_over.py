import pygame
from screens import BaseScreen
from components import TextBox


class GameOverScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.score = TextBox(
            (200, 100), "Score: " + str(self.store.score), color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.button1 = TextBox(
            (200, 100), "Again", color=(255, 0, 0), bgcolor=(120, 120, 120)
        )
        self.button2 = TextBox(
            (200, 100), "Quit", color=(0, 255, 0), bgcolor=(255, 140, 70)
        )
        self.button3 = TextBox(
            (200, 100), "Upload Score", color=(0, 255, 0), bgcolor=(255, 140, 70)
        )
        self.button1.rect.topleft = (200, 400)
        self.button2.rect.topleft = (500, 400)
        self.button3.rect.topleft = (300, 550)
        self.score.rect.topleft = (300, 200)
        self.sprites.add(self.button1, self.button2, self.button3, self.score)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)

    def update(self):
        pass

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button1.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "welcome"
            elif self.button2.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = False
            elif self.button3.rect.collidepoint(event.pos):
                self.running = False
                self.next_screen = "upload_score"
