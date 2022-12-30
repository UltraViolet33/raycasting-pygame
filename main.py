import pygame
import sys
import math
from settings import *
from map import *
from player import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.new_game()        
        
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        
    def update(self):
        self.player.update()
        pygame.display.flip()
        
        
    def draw(self):
        self.screen.fill("black")
        self.map.draw()
        self.player.draw()
        
    
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



# def draw_map():
#     for row in range(8):
#         for col in range(8):
#             square = row * MAP_SIZE + col
#             pygame.draw.rect(screen, (200, 200, 200) if MAP[square] == "#" else (100, 100, 100),
#                              (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE-2, TILE_SIZE-2))

#     # draw player
#     pygame.draw.circle(screen, (255, 0, 0), (int(player_x), int(player_y)), 8)

#     # player direction
#     pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (player_x -
#                      math.sin(player_angle) * 50, player_y + math.cos(player_angle) * 50), 3)

#     # player FOV
#     pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (player_x -
#                      math.sin(player_angle - HALF_FOV) * 50, player_y + math.cos(player_angle - HALF_FOV) * 50), 3)

#     pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (player_x -
#                      math.sin(player_angle + HALF_FOV) * 50, player_y + math.cos(player_angle + HALF_FOV) * 50), 3)


# # raycasting algo
# def cast_rays():
#     # most left angle of FOV
#     start_angle = player_angle - HALF_FOV

#     # loop over casted rays
#     for ray in range(CASTED_RAYS):
#         # cast ray step by step
#         for depth in range(MAX_DEPTH):
#             target_x = player_x - math.sin(start_angle) * depth
#             target_y = player_y + math.cos(start_angle) * depth

#             # convert target_y to map row
#             row = int(target_y / TILE_SIZE)
#             col = int(target_x / TILE_SIZE)

#             # calculate map square index
#             square = row * MAP_SIZE + col

#             if MAP[square] == "#":
#                 pygame.draw.rect(screen, (0, 255, 0), (col * TILE_SIZE,
#                                  row * TILE_SIZE, TILE_SIZE - 2, TILE_SIZE - 2))
#                 pygame.draw.line(screen, (255, 255, 0),
#                                  (player_x, player_y), (target_x, target_y))


#                 color = 255 / (1 + depth * depth * 0.0001)
                
#                 #fix fish effect
#                 depth *= math.cos(player_angle - start_angle)

#                 #CALCULATE wall height
#                 wall_height = 21000 / (depth + 0.0001)
                
                
#                 #fix stuck in wall
#                 if wall_height > SCREEN_HEIGHT:
#                     wall_height = SCREEN_HEIGHT
                
#                 #draw 3D rectangle by rectangle
#                 pygame.draw.rect(screen, (color, color, color), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2) - wall_height / 2, SCALE, wall_height))
#                 break

#     # increment angle by a single step
#         start_angle += STEP_ANGLE

# forward = True

# while True:

#     # quit
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0)
            
            
#     row = int(player_y / TILE_SIZE)
#     col = int(player_x / TILE_SIZE)

#     square = row * MAP_SIZE + col
    
#     if MAP[square] == "#":
#         if forward:
#             player_x -= -math.sin(player_angle) * 5
#             player_y -= math.cos(player_angle) * 5
#         else:
#             player_x += -math.sin(player_angle) * 5
#             player_y += math.cos(player_angle) * 5
            
        

#     # update 2D bck
#     pygame.draw.rect(screen, (0, 0, 0), (0, 0, SCREEN_HEIGHT, SCREEN_HEIGHT))

#     # update 3D bck
#     pygame.draw.rect(screen, (100, 100, 100), (SCREEN_HEIGHT,
#                      SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))
#     pygame.draw.rect(screen, (200, 200, 200), (SCREEN_HEIGHT, -
#                      SCREEN_HEIGHT / 2, SCREEN_HEIGHT, SCREEN_HEIGHT))

#     draw_map()

#     cast_rays()

#     # user inputs
#     

#     # set FPS
#     clock.tick(30)

#     # update display
#     pygame.display.flip()

