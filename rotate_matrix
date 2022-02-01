from typing import List
def rotate_matrix(matrix: List[List[int]]) -> None:
    size = len(matrix)
    for i in range(0, size // 2):
        for j in range(0, math.ceil(size / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[size - 1 - j][i]
            matrix[size - 1 - j][i] = matrix[size - 1 - i][size - 1 - j]
            matrix[size - 1 - i][size - 1 - j] = matrix[j][size - 1 - i]
            matrix[j][size - 1 - i] = temp