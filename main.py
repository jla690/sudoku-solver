def valid(board, randomNum, row, col):
    row_nums = board[row]
    if randomNum in row_nums:
        return False
    col_nums = []
    for i in range(9):
        col_nums.append(board[i][col])
    if randomNum in col_nums:
        return False

    rowOfSquare = (row // 3) * 3
    colOfSquare = (col // 3) * 3

    for i in range(rowOfSquare, rowOfSquare + 3):
        for j in range(colOfSquare, colOfSquare + 3):
            if board[i][j] == randomNum:
                return False
    return True


def print_board(board):
    for row in range(9):
        print("")
        print("|", end="")
        for col in range(9):
            print(board[row][col], end='|')
    print('\n')


def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None


def solve(board):
    row, col = find_empty(board)
    if row is None:
        return True

    for randomNum in range(1, 10):
        if valid(board, randomNum, row, col):
            board[row][col] = randomNum
            if solve(board):
                return True

        board[row][col] = 0
    return False


if __name__ == '__main__':
    game_board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    print("Before:", end="")
    print_board(game_board)
    if solve(game_board):
        print("After:", end="")
        print_board(game_board)
    else:
        print("Not solvable")
