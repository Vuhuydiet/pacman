from models.Map import Map
from models.MovingObject import Pacman, Ghost
import random
from utils.enums import CELL_TYPES

def on_update(map: Map, pacman: Pacman, ghosts: list[Ghost]):
  ghosts_next_positions = []
  total_expanded_nodes = 0
  for ghost in ghosts:
    next_position = ghost.target_position
    expanded_nodes = 0
    if ghost.target_position == ghost.position:
      next_position, expanded_nodes = ghost.moving_strategy(ghost.position, pacman.position, map, ghosts_next_positions) 

    ghost.update(next_position)
    ghosts_next_positions.append(next_position)
    
    if expanded_nodes is not None:
      total_expanded_nodes += expanded_nodes
    
  new_pacman_position = pacman.moving_strategy(pacman.position, map)
  if map.is_food(new_pacman_position):
    map.collect_gold(new_pacman_position)
    pacman.score += 1

  if new_pacman_position in ghosts_next_positions:
    pacman.lives -= 1
    empty_cells = [cell for cell in map.get_cells_of_type(CELL_TYPES['EMPTY']) if cell not in ghosts_next_positions]
    new_pacman_position = random.choice(empty_cells) if empty_cells else pacman.position
    pacman.set_position(new_pacman_position)
    print(new_pacman_position)
  else: 
    pacman.update(new_pacman_position)
  
  return total_expanded_nodes

