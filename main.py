class Board:
    def __init__(self):
        self.board = [
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

    def valid(self, randomNum, row, col):
        row_nums = self.board[row]
        if randomNum in row_nums:
            return False
        col_nums = []
        for i in range(9):
            col_nums.append(self.board[i][col])
        if randomNum in col_nums:
            return False

        rowOfSquare = (row // 3) * 3
        colOfSquare = (col // 3) * 3

        for i in range(rowOfSquare, rowOfSquare + 3):
            for j in range(colOfSquare, colOfSquare + 3):
                if self.board[i][j] == randomNum:
                    return False
        return True

    def print_board(self):
        for row in range(9):
            print("")
            print("|", end="")
            for col in range(9):
                print(self.board[row][col], end='|')
        print('\n')

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col
        return None, None

    def solve(self):
        row, col = self.find_empty()
        if row is None:
            return True

        for randomNum in range(1, 10):
            if self.valid(randomNum, row, col):
                self.board[row][col] = randomNum
                if self.solve():
                    return True

            self.board[row][col] = 0
        return False


if __name__ == '__main__':
    game_board = Board()
    print("Before:", end="")
    game_board.print_board()
    if game_board.solve():
        print("After:", end="")
        game_board.print_board()
    else:
        print("Not solvable")
