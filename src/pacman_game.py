import time
import tracemalloc
from utils.pygame_renderer import PygameRenderer
from models.Map import Map
from models.MovingObject import Ghost, Pacman
from utils.load_map import load
import utils.game_logic as game_logic

from moving_strategies.bfs import bfs
from moving_strategies.iddfs import iddfs
from moving_strategies.ucs import ucs
from moving_strategies.a_star import a_star
from moving_strategies.pygame_user_input import pygame_user_input

from utils.enums import *

def initialize_level(level):
    map_data, pacman_position, ghosts_positions = load('assets/maps/map2.txt')  
    maze_map = Map(map_data)
    
    ghosts = []
    
    if level == 1:
        pacman = Pacman(pacman_position, lambda pos, map: pos)
        ghosts.append(Ghost(ghosts_positions[0], bfs, GHOST_NAMES['BLUE']))
        
    elif level == 2:
        pacman = Pacman(pacman_position, lambda pos, map: pos)
        ghosts.append(Ghost(ghosts_positions[0], iddfs, GHOST_NAMES['PINK']))
        
    elif level == 3:
        pacman = Pacman(pacman_position, lambda pos, map: pos)
        ghosts.append(Ghost(ghosts_positions[0], ucs, GHOST_NAMES['ORANGE']))
        
    elif level == 4:
        pacman = Pacman(pacman_position, lambda pos, map: pos)
        ghosts.append(Ghost(ghosts_positions[0], a_star, GHOST_NAMES['RED']))
        
    elif level == 5:
        pacman = Pacman(pacman_position, lambda pos, map: pos)
        strategies = [bfs, iddfs, ucs, a_star]
        names = list(GHOST_NAMES.values())
        num_ghosts = len(ghosts_positions)
        num_strategies = len(strategies)
        
        for i in range(num_ghosts):
            ghosts.append(Ghost(ghosts_positions[i], strategies[i % num_strategies], names[i % len(names)]))
            
    elif level == 6:
        pacman = Pacman(pacman_position, pygame_user_input)
        strategies = [bfs, iddfs, ucs, a_star]
        names = list(GHOST_NAMES.values())
        num_ghosts = len(ghosts_positions)
        num_strategies = len(strategies)
        
        for i in range(num_ghosts):
            ghosts.append(Ghost(ghosts_positions[i], strategies[i % num_strategies], names[i % len(names)]))
    
    return maze_map, pacman, ghosts

def run_game(level):
    renderer = PygameRenderer()
    maze_map, pacman, ghosts = initialize_level(level)
    
    if level < 6:
        renderer.set_fps(2)
    else:
        renderer.set_fps(4)
        
    is_running = True
    metrics = {"search_time": 0.0, "expanded_nodes": 0, "memory_usage": "0 KB"}
    
    while is_running:
        keys = renderer.handle_events()
        
        start_time = time.time()
        tracemalloc.start()
        
        if level == 6:
            pacman.moving_strategy = lambda pos, maze_map: pygame_user_input(pos, maze_map, keys)
        
        expanded_nodes = game_logic.on_update(maze_map, pacman, ghosts)
        
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()
        
        metrics["search_time"] = end_time - start_time
        metrics["expanded_nodes"] = expanded_nodes if expanded_nodes is not None else 0
        metrics["memory_usage"] = f"{peak / 1024:.2f} KB"
            
        renderer.render_game(maze_map, pacman, ghosts, level, metrics)
        
        if pacman.lives <= 0:
            is_running = False
            renderer.show_game_over(pacman.score)
            
def main():
    renderer = PygameRenderer()
    
    while True:
        level = renderer.get_menu_input()
        
        run_game(level)
        
if __name__ == "__main__":
    main()