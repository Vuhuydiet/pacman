
def load(file_path: str) -> tuple[list[str], tuple[int, int], list[tuple[int, int]]]:
  with open(file_path, 'r') as file:
    lines = file.readlines()
    map_data = [line.strip() for line in lines]
    map_data = [line.replace('\n', '') for line in map_data]
    map_data = [line.replace('\r', '') for line in map_data]
  
    pacman =  None
    ghosts = []
    for i, line in enumerate(map_data):
      for j, cell in enumerate(line):
        if cell == 'V':
          pacman = (i, j)
        elif cell == 'G':
          ghosts.append((i, j))
    map_data = [[ch if ch not in ['V', 'G'] else '.' for ch in line] for line in map_data]
    
    if pacman is None:
      raise ValueError("Pacman not found in the map")
    if len(ghosts) == 0:
      raise ValueError("No ghosts found in the map")
    
    return (map_data, pacman, ghosts)
    