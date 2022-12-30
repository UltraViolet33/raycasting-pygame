import pygame
import math
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.forward = True
        
        
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= 0.1

        if keys[pygame.K_RIGHT]:
            self.angle += 0.1

        if keys[pygame.K_z]:
            self.forward = True
            self.x += - math.sin(self.angle) * 5
            self.y += math.cos(self.angle) * 5

        if keys[pygame.K_s]:
            self.forward = False
            self.x -= - math.sin(self.angle) * 5
            self.y -= math.cos(self.angle) * 5
        
        
    def draw(self):
        pygame.draw.circle(self.game.screen, (255, 0, 0), (int(self.x), int(self.y)), 8)
        
    def update(self):
        self.move()