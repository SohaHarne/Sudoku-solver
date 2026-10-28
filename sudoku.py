def print_board(board):
    """Prints the Sudoku board nicely in the terminal."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Scans the board for the first cell containing 0 (empty)."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None

def is_valid(board, row, col, num):
    """Checks if placing 'num' is valid according to Sudoku rules."""
    # 1. Check row
    if num in board[row]:
        return False
        
    # 2. Check column
    if num in [board[r][col] for r in range(9)]:
        return False
        
    # 3. Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
                
    return True

def solve_sudoku(board):
    """Recursively solves the Sudoku puzzle using backtracking."""
    row, col = find_empty(board)
    
    # If no empty cell is left, it's solved!
    if row is None:
        return True
    
    # Try digits 1 through 9
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num # Tentatively place number
            
            if solve_sudoku(board):
                return True
            
            # Backtrack if it leads to a dead end
            board[row][col] = 0
            
    return False

# Sample incomplete puzzle (0 represents empty cells)
sample_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("--- Sudoku Board BEFORE Solving ---")
print_board(sample_board)
print("\n" + "="*31 + "\n")

if solve_sudoku(sample_board):
    print("--- Sudoku Board AFTER Solving ---")
    print_board(sample_board)
else:
    print("No solution exists for this board!")