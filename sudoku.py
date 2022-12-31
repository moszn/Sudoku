def find_empty_cell(puzzle):
    """
    Finds the first empty cell in the puzzle by iterating through each row and column.
    Returns the row and column indices of the empty cell, or (None, None) if no empty cells are found.
    """
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == -1:
                return i, j
    return None, None

def is_valid_guess(puzzle, guess, row, col):
    """
    Determines if the given guess is a valid number to place in the given cell (row, col) of the puzzle.
    Returns True if the guess is valid, False otherwise.
    """
    # Check if the guess is already in the same row
    if guess in puzzle[row]:
        return False
    
    # Check if the guess is already in the same column
    col_values = [puzzle[i][col] for i in range(9)]
    if guess in col_values:
        return False
    
    # Check if the guess is already in the same 3x3 box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if puzzle[i][j] == guess:
                return False
    
    # If none of the above checks fail, the guess is valid
    return True

def solve_sudoku(puzzle):
    """
    Recursive function to solve the given Sudoku puzzle.
    Returns True if a solution is found, False otherwise.
    """
    # Find the next empty cell
    row, col = find_empty_cell(puzzle)
    
    # If there are no more empty cells, the puzzle is solved
    if row is None:
        return True

    # Try each number (1-9) as a guess for the empty cell
    for guess in range(1, 10):
        if is_valid_guess(puzzle, guess, row, col):
            # If the guess is valid, place it in the puzzle and try to solve the rest of the puzzle
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                # If the puzzle can be solved with this guess, return True
                return True
            
            # If the puzzle cannot be solved with this guess, reset the cell to empty and try the next guess
            puzzle[row][col] = -1

    # If no guesses work, return False
    return False

if __name__ == '__main__':
    easy_puzzle = [
    [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
    [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

    [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

    [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    [1, -1, 9,   -1, -1, -1,   2, -1, -1]
]

    ##print(solve_sudoku(easy_puzzle))
    ##print(easy_puzzle)

    hard_puzzle = [
    [-1, -1, -1,   -1, -1, -1,   -1, 7, 3],
    [-1, -1, 3,   6, 9, -1,   -1, -1, -1],
    [7, 4, -1,   -1, -1, -1,   -1, -1, -1],

    [-1, 6, -1,   -1, -1, 3,   -1, 9, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, 1,   -1, -1, 6],

    [6, -1, -1,   3, -1, -1,   -1, -1, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, 4, -1],
    [-1, -1, -1,   -1, -1, -1,   -1, -1, -1]
]

    print(solve_sudoku(hard_puzzle))
    print(hard_puzzle)
