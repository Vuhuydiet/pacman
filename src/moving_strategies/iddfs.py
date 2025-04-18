from utils.benchmark import strategy_benchmark
from utils.add_tuple import add
from utils.enums import DIRECTIONS
from models.Map import Map

@strategy_benchmark
def iddfs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:
  
  n_expanded_nodes = 0
  
  # def dfs(current, visited, depth, limit) -> tuple[int, int]:
  #   if depth > limit:
  #     return None

  #   nonlocal n_expanded_nodes
  #   n_expanded_nodes += 1

  #   for d in DIRECTIONS.values():
  #     new_cell = add(current, d)
  #     if not maze.contains_cell(new_cell) or new_cell in visited or maze.is_wall(new_cell):
  #       continue
  #     if depth == 0 and new_cell in restricted_cells:
  #       continue

  #     if new_cell == pacman_pos:
  #       return new_cell
      
  #     visited.add(new_cell)
  #     result = dfs(new_cell, visited, depth + 1, limit)
  #     if result is not None:
  #       return new_cell
  #     visited.remove(new_cell)
  #   return None

  # for depth in range(1, maze.N * maze.M):
  #   visited = set()
  #   visited.add(position)
  #   res = dfs(position, visited, 0, depth)
  #   if res != None:
  #     return res, n_expanded_nodes
    
  return position, n_expanded_nodes