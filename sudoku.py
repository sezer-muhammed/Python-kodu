import numpy as np

sudoku = [
    [1, 2, 3, 7, 8, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 4, 8, 0, 0, 0, 0, 0, 0],
    [2, 0, 1, 3, 5, 7, 8, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0],
    [9, 3, 1, 0, 0, 0, 8, 6, 2]]

sudoku = np.array(sudoku)


def uygun_mu(y, x, n):
    global sudoku
    for i in range(9):
        if sudoku[i][x] == n:
            return False

    for i in range(9):
        if sudoku[y][i] == n:
            return False

    rangeX = (x // 3) * 3
    rangeY = (y // 3) * 3
    for i in range(rangeX, rangeX + 3):
        for j in range(rangeY, rangeY + 3):
            if sudoku[j][i] == n:
                return False
    return True


def solve():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if uygun_mu(i, j, k):
                        sudoku[i][j] = k
                        solve()
                        sudoku[i][j] = 0
                return
    print(sudoku)


solve()
