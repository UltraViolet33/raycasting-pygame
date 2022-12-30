import math

SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2

FOV = math.pi / 3
HALF_FOV = FOV / 2

MAP_SIZE = 8

TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS

MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)


SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS