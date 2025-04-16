from utils.add_tuple import add
from utils.enums import DIRECTIONS
from models.Map import Map

def dfs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> dict[tuple[int, int], tuple[int, int]]:
  prev = {}
  prev[position] = position
  
  def dfs_imp(current: tuple[int, int]) -> tuple[int, int]:
    if current in restricted_cells:
      return None
    
    for d in DIRECTIONS.values():
      new_cell = add(current, d)
      if not maze.contains_cell(new_cell) or new_cell in prev or maze.is_wall(new_cell):
        continue
      
      prev[new_cell] = current
      if new_cell == pacman_pos:
        return new_cell
      result = dfs_imp(new_cell)
      if result is not None:
        return result
    
    return None
  
  dfs_imp(position)
  return prev