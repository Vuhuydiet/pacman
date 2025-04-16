import os

from models.Map import Map
from models.MovingObject import Pacman, Ghost

def to_string(map, pacman, ghosts):
  res = ""
  ghosts_positions = [ghost.position for ghost in ghosts]
  for i in range(map.N):
    for j in range(map.M):
      if (i, j) == pacman.position:
        res += 'V'
      elif (i, j) in ghosts_positions:
        res += 'G'
      else:
        res += map.get_cell(i, j)
    res += '\n'
  return res

def console_render(map: Map, pacman: Pacman, ghosts: list[Ghost]):
  # clear screen
  # os.system('cls' if os.name == 'nt' else 'clear')

  print("Score:", pacman.score)
  print("Lives:", pacman.lives)
  
  map_string = to_string(map, pacman, ghosts)
  print(map_string)

def on_render(map: Map, pacman: Pacman, ghosts: list[Ghost]):
  console_render(map, pacman, ghosts)