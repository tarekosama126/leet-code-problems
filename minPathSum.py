from typing import List
def minPathSum(grid: List[List[int]]):
    row, col = len(grid), len(grid[0])
    Matrix = [[0 for x in range(col)] for y in range(row)]
    Matrix[0][0] = grid[0][0]
    for j in range(1, col):
        Matrix[0][j] = Matrix[0][j - 1] + grid[0][j]
    for j in range(1, row):
        Matrix[j][0] = Matrix[j - 1][0] + grid[j][0]
    for i in range(1, row):
        for j in range(1, col):
            Matrix[i][j] = min(Matrix[i - 1][j], Matrix[i][j - 1]) + grid[i][j]
    return Matrix[row - 1][col - 1]