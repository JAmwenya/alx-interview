#!/usr/bin/python3
"""
N-Queens Problem: Solve the N-Queens puzzle
"""

import sys


def is_safe(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe.
    Args:
        board (list): The chessboard.
        row (int): Row index.
        col (int): Column index.
    Returns:
        bool: True if safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """
    Recursively solve the N-Queens problem.
    Args:
        N (int): Size of the board (N x N).
        row (int): Current row.
        board (list): Board state with queens' positions.
        solutions (list): Collected solutions.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1  # Backtrack


def nqueens(N):
    """
    Solve the N-Queens problem and print all solutions.
    Args:
        N (int): Size of the board (N x N).
    """
    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
