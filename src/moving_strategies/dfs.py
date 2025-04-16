from utils.add_tuple import add
from utils.enums import DIRECTIONS
from models.Map import Map

def dfs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[int, int]:
  
  visited = set()  
  visited.add(position)
  def dfs_imp(current: tuple[int, int]) -> tuple[int, int]:
    if current in restricted_cells:
      return None
    
    for d in DIRECTIONS.values():
      new_cell = add(current, d)
      if not maze.contains_cell(new_cell) or new_cell in visited or maze.is_wall(new_cell):
        continue

      visited.add(new_cell)
      if new_cell == pacman_pos:
        return new_cell
      result = dfs_imp(new_cell)
      if result is not None:
        return new_cell
    
    return None

  res = dfs_imp(position)
  if res is None:
    return position  
  return res