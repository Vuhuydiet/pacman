from models.Map import Map
from models.MovingObject import Pacman, Ghost

def on_update(map: Map, pacman: Pacman, ghosts: list[Ghost]):
  new_pacman_position = pacman.moving_strategy(pacman.position, map)
  
  ghosts_next_positions = []
  total_expanded_nodes = 0
  
  for ghost in ghosts:
    next_position, expanded_nodes = ghost.moving_strategy(ghost.position, pacman.position, map, ghosts_next_positions)
    
    ghost.update(next_position)
    ghosts_next_positions.append(next_position)
    if expanded_nodes is not None:
      total_expanded_nodes += expanded_nodes
    
  if map.is_food(new_pacman_position):
    map.collect_gold(new_pacman_position)
    pacman.score += 1

  if new_pacman_position in ghosts_next_positions:
    pacman.lives -= 1
  
  pacman.update(new_pacman_position)
  
  return total_expanded_nodes

