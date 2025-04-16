from utils.benchmark import strategy_benchmark
from models.Map import Map

@strategy_benchmark
def a_star(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:
  
  return position, 0