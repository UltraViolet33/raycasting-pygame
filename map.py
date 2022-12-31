import pygame
from settings import *


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = MAP

    def draw(self):
        for row in range(8):
            for col in range(8):
                square = row * MAP_SIZE + col
                pygame.draw.rect(self.game.screen, (200, 200, 200) if self.mini_map[square] == "#" else (
                    100, 100, 100), (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE-2, TILE_SIZE-2))
