#!/usr/bin/python3
"""
The N qeens pzzle is the challenge of placing N non-attacking qeens
on an NxN chessboard. Write a program that solves the N queens problem.
"""


def generate_solutions(row, column):
    solution = [[]]
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    return solution


def place_queen(queen, column, prev_solution):
    safe_position = []
    for array in prev_solution:
        for x in range(column):
            if is_safe(queen, x, array):
                safe_position.append(array + [x])
    return safe_position


def is_safe(q, x, array):
    if x in array:
        return (False)
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqeens N")
        exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            exit(1)

        solutions = generate_solutions(n, n)
        for solution in solutions:
            clean = []
            for q, x in enumerate(solution):
                clean.append([q, x])
            print(clean)
    except ValueError:
        print("N must be a number")
        exit(1)
