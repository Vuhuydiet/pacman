from models.Map import Map
from utils.add_tuple import add

def user_input(position: tuple[int, int], maze: Map) -> tuple[int, int]:
  moves = {
      "w": (-1, 0),  # Up
      "s": (1, 0),   # Down
      "a": (0, -1),  # Left
      "d": (0, 1)    # Right
  }

  print("Enter move (w: up, s: down, a: left, d: right): ", end="")
  user_move = input().strip().lower()

  if user_move not in moves:
    print("Invalid input. Please use 'w', 's', 'a', or 'd'.")
    return position

  new_position = add(position, moves[user_move])
  if not maze.contains_cell(new_position) or maze.is_wall(new_position):
    print("Invalid move. You hit a wall or are out of bounds.") 
    return position 

  return new_position