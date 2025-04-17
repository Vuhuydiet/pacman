import random
from utils.benchmark import strategy_benchmark
from models.Map import Map
from utils.enums import DIRECTIONS
from utils.add_tuple import add

@strategy_benchmark
def random_move(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:
  available_moves = []
  n_expanded_nodes = 1  # Only expanding current node
  
  for d in DIRECTIONS.values():
    new_cell = add(position, d)
    if not maze.contains_cell(new_cell) or maze.is_wall(new_cell):
      continue
    if new_cell in restricted_cells and new_cell != position:
      continue
    available_moves.append(new_cell)
  
  if available_moves:
    return random.choice(available_moves), n_expanded_nodes
  else:
    return position, n_expanded_nodes