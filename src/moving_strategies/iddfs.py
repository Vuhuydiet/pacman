from utils.benchmark import strategy_benchmark
from utils.add_tuple import add
from utils.enums import DIRECTIONS
from models.Map import Map

@strategy_benchmark
def iddfs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:
  
  n_expanded_nodes = 0
  
  def dfs(current, met_at, depth, limit) -> tuple[int, int]:
    if depth > limit:
      return None

    nonlocal n_expanded_nodes
    n_expanded_nodes += 1

    for d in DIRECTIONS.values():
      new_cell = add(current, d)
      if not maze.contains_cell(new_cell) or met_at.get(new_cell, 1e9) <= depth + 1 or maze.is_wall(new_cell):
        continue
      if depth == 0 and new_cell in restricted_cells:
        continue

      if new_cell == pacman_pos:
        return new_cell
      
      met_at[new_cell] = depth + 1
      result = dfs(new_cell, met_at, depth + 1, limit)
      if result is not None:
        return new_cell
    return None

  for depth in range(1, maze.N * maze.M):
    met_at = {}
    met_at[position] = 0
    res = dfs(position, met_at, 0, depth)
    if res != None:
      return res, n_expanded_nodes
    
  return position, n_expanded_nodes