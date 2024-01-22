def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        return [board[i][:] for i in range(n)]

    solutions = []

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solutions.extend(solve_n_queens_util(board, col + 1, n))
            board[i][col] = 0

    return solutions

def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = solve_n_queens_util(board, 0, n)
    return solutions

n = 8
solutions = solve_n_queens(n)
for solution in solutions:
    for row in solution:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))
    print("\n")
