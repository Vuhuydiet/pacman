from utils.benchmark import strategy_benchmark

from models.Map import Map
import queue
from utils.enums import DIRECTIONS
from utils.add_tuple import add


@strategy_benchmark
def bfs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:
  n_expanded_nodes = 0  
  
  q = queue.Queue()
  prev = {}

  q.put(position)
  prev[position] = position
  while not q.empty():
    current = q.get()
    n_expanded_nodes += 1
    found = False
    for d in DIRECTIONS.values():
      new_cell = add(current, d)
      if not maze.contains_cell(new_cell) or new_cell in prev or maze.is_wall(new_cell):
        continue
      if current == position and new_cell in restricted_cells and new_cell != position:
        continue
      
      prev[new_cell] = current
      q.put(new_cell)
      
      if new_cell == pacman_pos:
        found = True
        break
    if found:
      break
  
  cur_pos = pacman_pos
  prev_pos = prev[cur_pos]
  while prev_pos != position:
    cur_pos = prev_pos
    prev_pos = prev[cur_pos]
  
  return cur_pos, n_expanded_nodes
    