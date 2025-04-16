from models.Map import Map
from models.MovingObject import Pacman

def on_update(map: Map, pacman: Pacman, ghosts: list[Pacman]):
  new_pacman_position = pacman.moving_strategy(pacman.position, map)
  
  ghosts_next_positions = [ghost.position for ghost in ghosts]
  for ghost in ghosts:
    next_position = ghost.moving_strategy(ghost.position, pacman.position, map, ghosts_next_positions)
    
    ghost.position = next_position
    ghosts_next_positions.append(next_position)
    
    
  if map.is_food(new_pacman_position):
    map.collect_gold(new_pacman_position)
    pacman.score += 1

  if new_pacman_position in ghosts_next_positions:
    pacman.lives -= 1
  
  pacman.position = new_pacman_position
  
  