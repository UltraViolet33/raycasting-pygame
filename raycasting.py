import pygame
from settings import *


class Raycasting:
    def __init__(self, game, player, map):
        self.game = game
        self.player = player
        self.map = map

    def draw(self):
        start_angle = self.player.angle - HALF_FOV
        for ray in range(CASTED_RAYS):
            for depth in range(MAX_DEPTH):
                target_x = self.player.x - math.sin(start_angle) * depth
                target_y = self.player.y + math.cos(start_angle) * depth

                # convert target_y to map row
                row = int(target_y / TILE_SIZE)
                col = int(target_x / TILE_SIZE)

                # calculate map square index
                square = row * MAP_SIZE + col

                if self.map.mini_map[square] == "#":

                    color = 255 / (1 + depth * depth * 0.0001)
                    # fix fish effect
                    depth *= math.cos(self.player.angle - start_angle)
                    wall_height = 21000 / (depth + 0.0001)

                    if wall_height > SCREEN_HEIGHT:
                        wall_height = SCREEN_HEIGHT

                    pygame.draw.rect(self.game.screen, (color, color, color), (
                        SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2) - wall_height / 2, SCALE, wall_height))
                    break
            start_angle += STEP_ANGLE
