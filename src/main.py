import utils
import utils.game_logic
import utils.load_map
import utils.renderer

from models.Map import Map
from models.MovingObject import Ghost, Pacman

from moving_strategies.user_input import user_input
from moving_strategies.bfs import bfs 
from moving_strategies.dfs import dfs
from moving_strategies.ucs import ucs
from moving_strategies.a_star import a_star


def initialize():
  map_data, pacman_position, ghosts_positions = utils.load_map.load('assets/maps/map1.txt')  
  
  map = Map(map_data)
  
  pacman = Pacman(pacman_position, user_input)
  
  idx = 0
  moving_strategies = [bfs, dfs, ucs, a_star]
  ghosts = []
  for ghost_position in ghosts_positions:
    ghosts.append(Ghost(ghost_position, moving_strategies[idx], f'Ghost {idx}'))
    idx = (idx + 1) % 4

  return map, pacman, ghosts  
  
def main():
  map, pacman, ghosts = initialize()
  
  is_running = True
  utils.renderer.on_render(map, pacman, ghosts)
  while is_running:
    utils.game_logic.on_update(map, pacman, ghosts)
    utils.renderer.on_render(map, pacman, ghosts)
    
    if pacman.lives <= 0:
      is_running = False


if __name__ == '__main__':
  main()    
    