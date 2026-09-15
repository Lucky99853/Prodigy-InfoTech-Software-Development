# Task-04: Sudoku Solver

def print_grid(grid):
    print("\nSolved Sudoku:")
    for row in grid:
        print(" ".join(map(str, row)))


def is_valid(grid, row, col, num):
    # Check row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:

                # Try numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        # Recursively solve the remaining grid
                        if solve_sudoku(grid):
                            return True

                        # Backtrack
                        grid[row][col] = 0

                return False

    return True


# Unsolved Sudoku
grid = [
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

print("Unsolved Sudoku:")
for row in grid:
    print(" ".join(map(str, row)))

if solve_sudoku(grid):
    print_grid(grid)
else:
    print("\nNo solution exists for this Sudoku.")