from utils.enums import CELL_TYPES

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