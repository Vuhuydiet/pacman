from models.Map import Map
from models.MovingObject import Pacman
from moving_strategies import random

def _get_next_position(moves: dict[tuple[int, int], tuple[int, int]], initial_position, destination_position) -> tuple[int, int]:
  cur = destination_position
  prev = moves[destination_position]
  while prev != initial_position:
    cur = prev
    prev = moves[cur]
  return cur

def on_update(map: Map, pacman: Pacman, ghosts: list[Pacman]):
  new_pacman_position = pacman.moving_strategy(pacman.position, map)
  
  ghosts_next_positions = []
  for ghost in ghosts:
    moves = ghost.moving_strategy(ghost.position, pacman.position, map, ghosts_next_positions)
    
    if pacman.position not in moves:
      moves = random.move_randomly(ghost.position, pacman.position, map, ghosts_next_positions)

    next_position = _get_next_position(moves, ghost.position, pacman.position)

    ghost.position = next_position
    ghosts_next_positions.append(next_position)
    
    
  if map.is_food(new_pacman_position):
    map.collect_gold(new_pacman_position)
    pacman.score += 1

  if new_pacman_position in ghosts_next_positions:
    pacman.lives -= 1
  
  pacman.position = new_pacman_position
  
  