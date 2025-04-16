from models.Map import Map
import queue
from utils.enums import DIRECTIONS
from utils.add_tuple import add

def bfs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> dict[tuple[int, int], tuple[int, int]]:
  q = queue.Queue()
  prev = {}
  
  q.put(position)
  prev[position] = position
  while not q.empty():
    current = q.get()
    for d in DIRECTIONS.values():
      new_cell = add(current, d)
      if not maze.contains_cell(new_cell) or new_cell in prev or maze.is_wall(new_cell):
        continue
      if new_cell in restricted_cells:
        continue
      prev[new_cell] = current
      q.put(new_cell)
      if new_cell == pacman_pos:
        break
  
  return prev
    