import pygame
from utils.add_tuple import add
from utils.enums import DIRECTIONS

def pygame_user_input(position, map, keys=None):
    if keys is None:
        return position
    
    new_position = position
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        new_position = add(position, DIRECTIONS['UP'])
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        new_position = add(position, DIRECTIONS['DOWN'])
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        new_position = add(position, DIRECTIONS['LEFT'])
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        new_position = add(position, DIRECTIONS['RIGHT'])
    
    if not map.contains_cell(new_position) or map.is_wall(new_position):
        return position
        
    return new_position