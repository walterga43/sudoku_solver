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
    # Checks all numbers in the same column 
    for r in range(9):
      if num == self.puzzle_grid[r][col]:
        return False
    
    # Checks all numbers in the same row
    for c in range(9):
      if num == self.puzzle_grid[row][c]:
        return False

    box_row = (row // 3) * 3
    box_col = (col // 3) * 3

    for r in range(box_row, box_row+3):
      for c in range(box_col, box_col+3):
        if num == self.puzzle_grid[r][c]:
          return False
    return True


  def find_empty_cell(self):
    # Helper methof for solve to find empty cells
    for r in range(len(self.puzzle_grid)):
      for c in range(len(self.puzzle_grid[0])):
        if self.puzzle_grid[r][c] == 0:
          return (r,c)
    return None

  def solve(self):
    # Main solve method
    if self.find_empty_cell() is None:
      return True
    
    for i in range(1, 10):
      next_cells = self.find_empty_cell()
      r, c = next_cells[0], next_cells[1]
      if self.is_valid_move(r, c, i):
        self.puzzle_grid[r][c] = i

        if self.solve():
          return True

        self.puzzle_grid[r][c] = 0

    return False

def main():

  while True:
    
    print("Example Puzzle: 53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79")
    puzzle = input("Enter a puzzle (left to right with . representing empty cells)")
    if len(puzzle) != 81:
      print("Puzzle is not vaild. Please try again")
      continue
    solver = SudokuSolver()
    print("YOUR PUZZLE")
    print("--------------------------------")
    solver.load_puzzle(puzzle)
    solver.print_board()
    print()

    print("SOLVED PUZZLE")
    print("--------------------------------")
    solver.solve()
    solver.print_board()
    print()

    continue_puzzle = input("Would you like to enter another puzzle? (y/n):").strip().lower()
    if continue_puzzle == "n":
      break
if __name__ == "__main__":
  main()