from models.Map import Map
import queue
from utils.enums import DIRECTIONS
from utils.add_tuple import add

def move_randomly(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> dict[tuple[int, int], tuple[int, int]]:
  prev = {}
  
  prev[position] = position
  for d in DIRECTIONS.values():
    new_cell = add(position, d)
    if not maze.contains_cell(new_cell) or new_cell in prev or maze.is_wall(new_cell):
      continue
    if new_cell in restricted_cells:
      continue
    prev[new_cell] = position
    prev[pacman_pos] = new_cell
    break
  return prev
    