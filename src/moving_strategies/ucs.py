from utils.benchmark import strategy_benchmark
from models.Map import Map
from heapq import heappop, heappush

@strategy_benchmark
def ucs(position, pacman_pos, maze: Map, restricted_cells: list[tuple[int, int]]) -> tuple[tuple[int, int], int]:
  open_set = []
  heappush(open_set, (0, position))
  came_from = {}
  g_score = {position: 0}
  expanded_nodes = 0
  closed_set = set()

  while open_set:
    cost, current = heappop(open_set)

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
      return path[0], expanded_nodes if path else (position, expanded_nodes)


    for neighbor in maze.get_neighbors(current):
      if current == position and neighbor in restricted_cells:
                continue
      if neighbor in closed_set:
                continue

      tentative_g_score = g_score[current] + 1  
      if tentative_g_score < g_score.get(neighbor, float('inf')):
        came_from[neighbor] = current
        g_score[neighbor] = tentative_g_score
        heappush(open_set, (tentative_g_score, neighbor))
  return position, expanded_nodes