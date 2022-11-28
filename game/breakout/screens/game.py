import random
import pygame
from screens import BaseScreen

from ..components import Paddle, Ball, TileGroup
from components import TextBox


class GameScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.score = 0
        self.streak = 1

        # Create the paddle
        self.paddle = Paddle(200, 30, (0, 255, 0), limits=self.rect)

        # Create the ball
        self.ball = Ball(limits=self.rect)
        self.ball.speed = 8

        self.ball.angle = random.randint(0, 31416) / 10000

        # Create the tiles
        self.tiles = TileGroup(tile_width=120, tile_height=30)

        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

        self.sprites.update()
        collided = self.ball.collidetiles(self.tiles)
        if collided:
            self.score += self.streak
            self.streak += 1
        
        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)
        if caught_the_ball:
            self.streak = 1

        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.next_screen = "game_over"
            self.store.score = self.score

    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.speed = 10
                self.ball.angle = 1.5
