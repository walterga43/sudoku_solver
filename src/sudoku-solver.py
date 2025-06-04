class SudokuSolver:
  def __init__(self):
    self.puzzle_grid = [[0 for _ in range(9)] for _ in range(9)]

  def load_puzzle(self, puzzle_string):
    for i in range(len(puzzle_string)):
      row = i // 9
      col = i % 9
      if puzzle_string[i] != ".":
        self.puzzle_grid[row][col] = int(puzzle_string[i])
  
  def print_board(self):
    for r in range(9):
      for c in range(9):
        print(self.puzzle_grid[r][c], end=" ")
      print()

  def is_valid_move(self, row, col, num):
    # Checks all numbers in the same collum
    for r in range(9):
      if num == self.puzzle_grid[r][col]:
        return False
    
    # Checks all numbers in the same row
    for c in range(9):
      if num == self.puzzle_grid[row][c]:
        return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for i in range(box_row, box_row+3):
      if self.puzzle_grid[i][box_col] == num or self.puzzle_grid[i][box_col+1] == num or self.puzzle_grid[i][box_col+2] == num:
        return False
    return True


## def find_empty_cell(self):

## def solve(self):

if __name__ == "__main__":
  puzzle = "53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79"
  solver = SudokuSolver()
  solver.load_puzzle(puzzle)
  solver.print_board()