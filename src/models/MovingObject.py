
class MovingObject:
  def __init__(self, initial_position: tuple[int, int], moving_strategy):
    self.position = initial_position
    self.moving_strategy = moving_strategy
    
    
class Pacman(MovingObject):
  def __init__(self, initial_position: tuple[int, int], moving_strategy):
    super().__init__(initial_position, moving_strategy)
    self.lives = 3
    self.score = 0
  

class Ghost(MovingObject):
  def __init__(self, initial_position: tuple[int, int], moving_strategy, name):
    super().__init__(initial_position, moving_strategy)
    self.name = name
  