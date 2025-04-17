from utils.get_quads import get_quads, get_pacman_quads, get_ghost_quads
import pygame
from utils.subtract_tuple import subtract_tuple
from utils.enums import MOVEMENT_DIRECTIONS, YELLOW, CELL_SIZE

pygame.init()
sprite_sheet = pygame.image.load('assets/sprites/sprite_sheet.png')
quads = get_quads(sprite_sheet)

class MovingObject:
  def __init__(self, initial_position: tuple[int, int], moving_strategy):
    self.position = initial_position
    self.moving_strategy = moving_strategy
    
    
class Pacman(MovingObject):
  def __init__(self, initial_position: tuple[int, int], moving_strategy):
    super().__init__(initial_position, moving_strategy)
    self.lives = 3
    self.score = 0
    self.animations = get_pacman_quads(quads)
    self.frame = 0
    self.time = pygame.time.get_ticks()
    self.collapse = 20
    self.direction = MOVEMENT_DIRECTIONS['UP']

  def get_direction(self, new_position):
    delta = subtract_tuple(new_position, self.position)
    if delta[1] > 0:
      return MOVEMENT_DIRECTIONS['RIGHT']
    elif delta[1] < 0:
      return MOVEMENT_DIRECTIONS['LEFT']
    elif delta[0] > 0:
      return MOVEMENT_DIRECTIONS['DOWN']
    elif delta[0] < 0:
      return MOVEMENT_DIRECTIONS['UP']
    return self.direction

  def update(self, new_position):
    current_time = pygame.time.get_ticks()
    self.direction = self.get_direction(new_position)

    if current_time - self.time >= self.collapse:
      self.frame = (self.frame + 1) % len(self.animations[self.direction])
      self.time = current_time
    
    self.position = new_position

  def draw(self, screen):
    if self.lives > 0:
      screen.blit(self.animations[self.direction][self.frame], 
                  (self.position[1] * CELL_SIZE, self.position[0] * CELL_SIZE))
    else:
      rect = pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
      pygame.draw.rect(screen, YELLOW, rect)

  

class Ghost(MovingObject):
  def __init__(self, initial_position: tuple[int, int], moving_strategy, name):
    super().__init__(initial_position, moving_strategy)
    self.name = name
    self.animations = get_ghost_quads(quads)[name]
    self.direction = MOVEMENT_DIRECTIONS['UP']

  def get_direction(self, new_position):
    delta = subtract_tuple(new_position, self.position)
    if delta[1] > 0:
      return MOVEMENT_DIRECTIONS['RIGHT']
    elif delta[1] < 0:
      return MOVEMENT_DIRECTIONS['LEFT']
    elif delta[0] > 0:
      return MOVEMENT_DIRECTIONS['DOWN']
    elif delta[0] < 0:
      return MOVEMENT_DIRECTIONS['UP']
    return self.direction

  def update(self, new_position):
    self.direction = self.get_direction(new_position)
    self.position = new_position
  
  def draw(self, screen):
    screen.blit(self.animations[self.direction], (self.position[1] * CELL_SIZE, self.position[0] * CELL_SIZE))
    