def __init__(self):
  self.board = [[0 for _ in range(9)] for _ in range(9)]

def get_board():
  puzzle_file = open("sudoku_solver\data\puzzles.txt")
  puzzle = puzzle_file.read()
  print(puzzle)

## def load_puzzle(self, puzzle_string):

## def print_board(self):

## def is_valid_move(self, row, col, num):

## def find_empty_cell(self):

## def solve(self):

if __name__ == "__main__":
  get_board()