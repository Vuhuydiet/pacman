CELL_TYPES = {
  'EMPTY': '.',
  'WALL': '#',
  'PACMAN': 'V',
  'GHOST': 'G',
  'FOOD': 'o',
}

# Cardinal directions in (row, col) format
DIRECTIONS = {
  'U': (-1, 0),
  'D': (1, 0),
  'L': (0, -1),
  'R': (0, 1),
  'UP': (-1, 0),
  'DOWN': (1, 0),
  'LEFT': (0, -1),
  'RIGHT': (0, 1),
}

# Ghost colors
GHOST_COLORS = {
  'BLUE': (0, 0, 255),    # BFS
  'PINK': (255, 192, 203), # DFS/IDDFS
  'ORANGE': (255, 165, 0), # UCS
  'RED': (255, 0, 0)       # A*
}



# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 192, 203)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
DARK_BLUE = (0, 0, 139)

# Screen dimensions
CELL_SIZE = 48
INFO_HEIGHT = 60

# Window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 800

# Font sizes
FONT_SIZE = 20
BIG_FONT_SIZE = 36
TITLE_FONT_SIZE = 48

# FPS
FRAMES_PER_SECOND = 10

# Number levels
NUM_LEVELS = 6

# Sprite sheet dimensions
SPRITE_SHEET_ROWS = 7
SPRITE_SHEET_COLUMNS = 11
TILE_SIZE = 32

# Ghost names
GHOST_NAMES = {
    'BLUE': 'Blue Ghost',
    'PINK': 'Pink Ghost',
    'ORANGE': 'Orange Ghost',
    'RED': 'Red Ghost',
}

# Movement directions
MOVEMENT_DIRECTIONS = {
    'UP': 'UP',
    'DOWN': 'DOWN',
    'LEFT': 'LEFT',
    'RIGHT': 'RIGHT',
}