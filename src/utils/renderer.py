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
  print(to_string(map, pacman, ghosts))
  
  if (pacman.lives <= 0):
    print("-----------------------------------------------------------")
    print("------------------------- Game Over -----------------------")
    print("-----------------------------------------------------------")


def on_render(map: Map, pacman: Pacman, ghosts: list[Ghost]):
  console_render(map, pacman, ghosts)