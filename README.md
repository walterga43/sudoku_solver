# Sudoku Solver

A Python-based Sudoku puzzle solver that uses backtracking algorithm to solve standard 9x9 Sudoku puzzles.

## Features

- Solves any valid 9x9 Sudoku puzzle
- Interactive command-line interface
- Clear puzzle display before and after solving
- Input validation for puzzle format
- Supports multiple puzzle solving in a single session

## How It Works

The solver uses a backtracking algorithm that:
1. Finds empty cells in the puzzle
2. Tries numbers 1-9 in each empty cell
3. Validates each number against Sudoku rules (no duplicates in row, column, or 3x3 box)
4. Recursively solves the remaining puzzle
5. Backtracks if no valid solution is found for the current path

## Usage

### Running the Program

```bash
python sudoku_solver.py
```

### Input Format

Enter puzzles as a single string of 81 characters:
- Use digits 1-9 for filled cells
- Use periods (.) for empty cells
- Read left to right, top to bottom

**Example puzzle:**
```
53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79
```

### Sample Session

```
Example Puzzle: 53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79
Enter a puzzle (left to right with . representing empty cells): 53..7....6..195....98....6.8...6...34..8.3..17...2...6.6....28....419..5....8..79

YOUR PUZZLE
--------------------------------
5 3 0 0 7 0 0 0 0 
6 0 0 1 9 5 0 0 0 
0 9 8 0 0 0 0 6 0 
8 0 0 0 6 0 0 0 3 
4 0 0 8 0 3 0 0 1 
7 0 0 0 2 0 0 0 6 
0 6 0 0 0 0 2 8 0 
0 0 0 4 1 9 0 0 5 
0 0 0 0 8 0 0 7 9 

SOLVED PUZZLE
--------------------------------
5 3 4 6 7 8 9 1 2 
6 7 2 1 9 5 3 4 8 
1 9 8 3 4 2 5 6 7 
8 5 9 7 6 1 4 2 3 
4 2 6 8 5 3 7 9 1 
7 1 3 9 2 4 8 5 6 
9 6 1 5 3 7 2 8 4 
2 8 7 4 1 9 6 3 5 
3 4 5 2 8 6 1 7 9 

Would you like to enter another puzzle? (y/n):
```

## Requirements

- Python 3.x
- No external dependencies required

## Code Structure

### Classes

**SudokuSolver**
- `__init__()`: Initializes empty 9x9 grid
- `load_puzzle(puzzle_string)`: Loads puzzle from string input
- `print_board()`: Displays current puzzle state
- `is_valid_move(row, col, num)`: Validates if a number can be placed at given position
- `find_empty_cell()`: Finds next empty cell in the grid
- `solve()`: Main solving method using backtracking algorithm

### Functions

**main()**
- Handles user interaction and program flow
- Validates input format
- Manages multiple puzzle sessions

## Error Handling

- Input validation ensures puzzles are exactly 81 characters
- Invalid puzzles prompt user to try again
- Program continues until user chooses to exit

## License

This project is open source and available under standard usage terms.