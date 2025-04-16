from models.Map import Map

def a_star(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> dict[tuple[int, int], tuple[int, int]]:
  prev = {}
  
  prev[position] = position
  
  return prev