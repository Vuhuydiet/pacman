from utils.enums import CELL_TYPES, DIRECTIONS
from utils.add_tuple import add

class Map:
  def __init__(self, map: list[str]):
    self.__map = [list(row) for row in map]
    self.N = len(map)
    self.M = len(map[0])
    
  def contains_cell(self, cell: tuple[int, int]) -> bool:
    x, y = cell
    return 0 <= x < self.N and 0 <= y < self.M
    
  def is_wall(self, cell: tuple[int, int]) -> bool:
    if not self.contains_cell(cell):
      raise ValueError("Coordinates out of bounds")
    
    x, y = cell
    return self.__map[x][y] == CELL_TYPES['WALL']
  
  def is_empty(self, cell: tuple[int, int]) -> bool:
    if not self.contains_cell(cell):
      raise ValueError("Coordinates out of bounds")
    
    x, y = cell
    return self.__map[x][y] == CELL_TYPES['EMPTY']
  
  def is_food(self, cell: tuple[int, int]) -> bool:
    if not self.contains_cell(cell):
      raise ValueError("Coordinates out of bounds")
    
    x, y = cell
    return self.__map[x][y] == CELL_TYPES['FOOD']
  
  def collect_gold(self, cell):
    if not self.contains_cell(cell):
      raise ValueError("Coordinates out of bounds")
    if not self.is_food(cell):
      raise ValueError("Cell is not food")
    x, y = cell
    self.__map[x][y] = CELL_TYPES['EMPTY']
      
  # def to_string(self):
  #   return '\n'.join(["".join(row) for row in self.__map])
  
  def get_cell(self, x, y):
    if not self.contains_cell((x, y)):
      raise ValueError("Coordinates out of bounds")
    return self.__map[x][y]
  
  def get_neighbors(self, cell: tuple[int, int]) -> list[tuple[int, int]]:
    neighbors = []
    for d in DIRECTIONS.values():
      new_cell = add(cell, d)
      if self.contains_cell(new_cell) and not self.is_wall(new_cell):
        neighbors.append(new_cell)  
    
    return neighbors
  
  def get_cells_of_type(self, cell_type: str) -> list[tuple[int, int]]:
    if cell_type not in CELL_TYPES.values():
      raise ValueError("Invalid cell type")

    cells = []
    for i in range(self.N):
      for j in range(self.M):
        if self.__map[i][j] == cell_type:
          cells.append((i, j))
    return cells
