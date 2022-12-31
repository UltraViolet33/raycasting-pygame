import pygame
import sys
import math
from settings import *
from Map import *
from Player import *
from Raycasting import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = Raycasting(self, self.player, self.map)

    def update(self):
        self.player.update()

        pygame.display.flip()

    def draw(self):
        pygame.draw.rect(self.screen, (0, 0, 0),
                         (0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, (100, 100, 100), (SCREEN_HEIGHT,
                         SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))
        pygame.draw.rect(self.screen, (200, 200, 200), (SCREEN_HEIGHT, -
                         SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))

        self.map.draw()
        self.player.draw()
        self.raycasting.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
