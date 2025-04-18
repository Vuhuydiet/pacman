from utils.benchmark import strategy_benchmark
from models.Map import Map
from heapq import heappop, heappush

@strategy_benchmark
def a_star(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:

  def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

  open_set = []
  heappush(open_set, (0, position))
  came_from = {}
  g_score = {position: 0}
  f_score = {position: heuristic(position, pacman_pos)}
  expanded_nodes = 0  
  closed_set = set() 

  while open_set:
    _, current = heappop(open_set)

    if current in closed_set:
      continue 

    closed_set.add(current)
    expanded_nodes += 1 

    if current == pacman_pos:
      path = []
      while current in came_from:
        path.append(current)
        current = came_from[current]
      path.reverse()
      if len(path) == 0:
        return position, expanded_nodes
      return path[0], expanded_nodes

    for neighbor in maze.get_neighbors(current):
      if (current == position and neighbor in restricted_cells) or neighbor in closed_set:
        continue

      tentative_g_score = g_score[current] + 1
      if tentative_g_score < g_score.get(neighbor, float('inf')):
        came_from[neighbor] = current
        g_score[neighbor] = tentative_g_score
        f_score[neighbor] = tentative_g_score + heuristic(neighbor, pacman_pos)
        heappush(open_set, (f_score[neighbor], neighbor))

  return position, expanded_nodes