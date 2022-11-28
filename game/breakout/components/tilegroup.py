import math
import pygame
from .tile import Tile
import random


class TileGroup(pygame.sprite.Group):
    def __init__(self, tile_width=100, tile_height=30):
        super().__init__()

        self.tiles = []
        self.tile_count = random.randint(50, 100)
        for i in range(self.tile_count):
            x = (i % 8) * tile_width 
            y = math.floor(i / 8) * tile_height
            if random.randint(0, 10) != 3:
                tile = Tile(width=tile_width, height=tile_height)

                tile.move_to(x, y)

                self.tiles.append(tile)

        self.add(self.tiles)
