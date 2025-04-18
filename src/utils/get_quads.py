import pygame
from utils.enums import *

def get_quads(sprite_sheet, 
              row=SPRITE_SHEET_ROWS, 
              column=SPRITE_SHEET_COLUMNS, 
              tile_size=TILE_SIZE) -> list:
    quads = []

    for i in range(row):
        for j in range(column):
            x = j * tile_size
            y = i * tile_size
            rect = pygame.Rect(x, y, tile_size, tile_size)
            quad = sprite_sheet.subsurface(rect)

            scaled_quad = pygame.transform.scale(quad, (CELL_SIZE, CELL_SIZE))
            quads.append(scaled_quad)

    return quads

def get_pacman_quads(quads) -> dict:
    directions = [MOVEMENT_DIRECTIONS['LEFT'], 
                  MOVEMENT_DIRECTIONS['RIGHT'], 
                  MOVEMENT_DIRECTIONS['DOWN'],
                  MOVEMENT_DIRECTIONS['UP']]
    pacman_quads = {}

    for i in range(4):
        pacman_quads[directions[i]] = []
        for j in range(2):
            pacman_quads[directions[i]].append(quads[j * SPRITE_SHEET_COLUMNS + i])

    return pacman_quads

def get_ghost_quads(quads) -> dict:
    directions = [MOVEMENT_DIRECTIONS['UP'], 
                  MOVEMENT_DIRECTIONS['DOWN'], 
                  MOVEMENT_DIRECTIONS['LEFT'],
                  MOVEMENT_DIRECTIONS['RIGHT']]
    ghost_names = [GHOST_NAMES['RED'], GHOST_NAMES['PINK'], GHOST_NAMES['BLUE'], GHOST_NAMES['ORANGE']]
    ghost_quads = {}

    for i in range(4):
        ghost_quads[ghost_names[i]] = {}
        for j in range(2, 6):
            ghost_quads[ghost_names[i]][directions[j-2]] = quads[j * SPRITE_SHEET_COLUMNS + i]

    return ghost_quads
    
def get_food_quads(quads) -> list:
    food_quads = []
    
    for i in range(4, 6):
        for j in range(8, 11):
            quad = quads[j * SPRITE_SHEET_COLUMNS + i]
            food_quads.append(quad)

    return food_quads
