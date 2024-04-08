#!/usr/bin/python3
"""
This module contains an algorithm that resolves the N-Queen puzzle
using backtracking
"""

def is_safe(m_queen, nqueen):
    """Check if queens can or can't kill each other

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """
    for i in range(nqueen):
        if m_queen[i] == m_queen[nqueen] or abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False
    return True

def print_result(m_queen, nqueen):
    """Print the list with the Queens positions

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """
    res = []
    for i in range(nqueen):
        res.append([i, m_queen[i]])
    print(res)

def queen(m_queen, nqueen):
    """Recursive function that executes the Backtracking algorithm

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """
    if nqueen == len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while m_queen[nqueen] < len(m_queen) - 1:
        m_queen[nqueen] += 1
        if is_safe(m_queen, nqueen):
            if nqueen < len(m_queen):
                queen(m_queen, nqueen + 1)

def solve_n_queen(size):
    """Function that invokes the Backtracking algorithm

    Args:
        size: size of the chessboard

    """
    m_queen = [-1 for _ in range(size)]
    queen(m_queen, 0)

if __name__ == '__main__':
    import sys

    # Check for the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Try to convert the argument to an integer
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queen(size)
