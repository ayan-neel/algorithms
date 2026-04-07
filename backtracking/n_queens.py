def n_queens(row, board):
    # Base case: all queens placed
    if row == len(board):
        print_board(board)
        return  # Stop recursion for this branch

    for col in range(len(board[0])):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            n_queens(row + 1, board)  # Recurse to next row
            board[row][col] = 0  # Backtrack

def is_safe(board, row, col):
    # Check vertically upwards
    for r in range(row, -1, -1):
        if board[r][col] == 1:
            return False

    # Check positive diagonal (top-left)
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check negative diagonal (top-right)
    r, c = row, col
    while r >= 0 and c < len(board[0]):
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    return True


def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))


if __name__ == "__main__":
    n = 5
    board = [[0 for _ in range(n)] for _ in range(n)]
    n_queens(0, board)
