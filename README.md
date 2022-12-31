# Sudoku

This is a simple Sudoku solver implemented in Python. It uses a recursive backtracking algorithm to find a solution for a given Sudoku puzzle.

# Usage

To use the solver, you can either import the solve_sudoku function into your own code or run it as a standalone script.

As a standalone script
To run the solver as a standalone script, you can call the script with a Sudoku puzzle as a command line argument. The puzzle should be a 9x9 list of integers, with empty cells represented by -1. For example:

python sudoku_solver.py "[[-1, -1, 2,   3, -1, -1,   6, -1, -1],
                         [9, -1, -1,   -1, -1, -1,   -1, -1, 1],
                         [8, -1, -1,   -1, -1, -1,   -1, -1, -1],

                         [7, -1, -1,   -1, 2, 6,   -1, -1, -1],
                         [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
                         [-1, -1, -1,   1, 8, -1,   -1, -1, 3],

                         [-1, -1, -1,   -1, -1, -1,   -1, -1, 6],
                         [6, -1, -1,   -1, -1, -1,   -1, -1, 9],
                         [-1, -1, 3,   -1, -1, 5,   1, -1, -1]]"
The solver will print the solved puzzle to the console.

# As a library
To use the solver as a library in your own code, you can import the solve_sudoku function and pass it a Sudoku puzzle as a list of lists. For example:
from sudoku_solver import solve_sudoku

puzzle = [[-1, -1, 2, 3, -1, -1, 6, -1, -1],
          [9, -1, -1, -1, -1, -1, -1, -1, 1],
          [8, -1, -1, -1, -1, -1, -1, -1, -1],
          [7, -1, -1, -1, 2, 6, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, 1, 8, -1, -1, -1, 3],
          [-1, -1, -1, -1, -1, -1, -1, -1, 6],
          [6, -1, -1, -1, -1, -1, -1, -1, 9],
          [-1, -1, 3, -1, -1, 5, 1, -1, -1]]

solve_sudoku(puzzle)
print(puzzle)

This will print the solved puzzle to the console.
