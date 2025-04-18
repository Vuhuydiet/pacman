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

    self.visual_x = initial_position[1] * CELL_SIZE
    self.visual_y = initial_position[0] * CELL_SIZE
    self.target_position = initial_position
    self.speed = 4
    self.is_moving = False
    
    
class Pacman(MovingObject):
  def __init__(self, initial_position: tuple[int, int], moving_strategy):
    super().__init__(initial_position, moving_strategy)
    self.lives = 3
    self.score = 0
    self.animations = get_pacman_quads(quads)
    self.frame = 0
    self.time = pygame.time.get_ticks()
    self.collapse = 30
    self.direction = MOVEMENT_DIRECTIONS['RIGHT']

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
    
    if new_position != self.target_position:
      self.target_position = new_position
      self.direction = self.get_direction(new_position)
      self.is_moving = True
    
    if current_time - self.time >= self.collapse:
      self.frame = (self.frame + 1) % len(self.animations[self.direction])
      self.time = current_time
    
    if self.is_moving:
      target_x = self.target_position[1] * CELL_SIZE
      target_y = self.target_position[0] * CELL_SIZE
      
      dx = target_x - self.visual_x
      dy = target_y - self.visual_y
      
      if abs(dx) <= self.speed and abs(dy) <= self.speed:
        self.visual_x = target_x
        self.visual_y = target_y
        self.position = self.target_position
        self.is_moving = False
      else:
        if dx > 0:
          self.visual_x += min(self.speed, dx)
        elif dx < 0:
          self.visual_x -= min(self.speed, abs(dx))
          
        if dy > 0:
          self.visual_y += min(self.speed, dy)
        elif dy < 0:
          self.visual_y -= min(self.speed, abs(dy))

  def draw(self, screen):
    if self.lives > 0:
      screen.blit(self.animations[self.direction][self.frame], 
                  (self.visual_x, self.visual_y))
    else:
      rect = pygame.Rect(self.visual_x, self.visual_y, CELL_SIZE, CELL_SIZE)
      pygame.draw.circle(screen, YELLOW, rect.center, CELL_SIZE // 2)

  

class Ghost(MovingObject):
  def __init__(self, initial_position: tuple[int, int], moving_strategy, name):
    super().__init__(initial_position, moving_strategy)
    self.name = name
    self.animations = get_ghost_quads(quads)[name]
    self.direction = MOVEMENT_DIRECTIONS['RIGHT']

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
    if new_position != self.target_position:
      self.target_position = new_position
      self.direction = self.get_direction(new_position)
      self.is_moving = True
    
    if self.is_moving:
      target_x = self.target_position[1] * CELL_SIZE
      target_y = self.target_position[0] * CELL_SIZE
      
      dx = target_x - self.visual_x
      dy = target_y - self.visual_y
      
      if abs(dx) <= self.speed and abs(dy) <= self.speed:
        self.visual_x = target_x
        self.visual_y = target_y
        self.position = self.target_position
        self.is_moving = False
      else:
        if dx > 0:
          self.visual_x += min(self.speed, dx)
        elif dx < 0:
          self.visual_x -= min(self.speed, abs(dx))
          
        if dy > 0:
          self.visual_y += min(self.speed, dy)
        elif dy < 0:
          self.visual_y -= min(self.speed, abs(dy))
  
  def draw(self, screen):
    screen.blit(self.animations[self.direction], (self.visual_x, self.visual_y))
