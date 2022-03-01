from typing import List
def isValidSudoku(board: List[List[str]]) -> bool:
    # first validate the rows
    # i is rows and j is coloum
    for i in range(0, 9):
        char = []
        for j in range(0, 9):
            if board[i][j] in char:
                return False
            if board[i][j] != ".":
                char.append(board[i][j])
    # print ("ROW IS VALIDATED")
    # validate the coloums
    for i in range(0, 9):
        char = []
        for j in range(0, 9):
            if board[j][i] in char:
                return False
            if board[j][i] != ".":
                char.append(board[j][i])
    # print ("Coloum is validated IS VALIDATED")
    # validate the boxes
    for start in range(0, 9, 3):
        for end in range(0, 9, 3):
            char = []
            for i in range(0, 3):
                for j in range(0, 3):
                    if board[start + i][end + j] in char:
                        return False
                    if board[start + i][end + j] != ".":
                        char.append(board[start + i][end + j])
    # print("Box is validated")
    return True