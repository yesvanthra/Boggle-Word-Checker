def find_word(board, word):
    def boogle(row, col, index):
        if index == len(word):
            return True
        if (
            row < 0
            or row >= len(board)
            or col < 0
            or col >= len(board[0])
            or board[row][col] != word[index]
        ):
            return False
        temp, board[row][col] = board[row][col], '#'
        format = (
            boogle(row + 1, col, index + 1)
            or boogle(row - 1, col, index + 1)
            or boogle(row, col + 1, index + 1)
            or boogle(row, col - 1, index + 1)
            or boogle(row + 1, col + 1, index + 1)
            or boogle(row - 1, col - 1, index + 1)
            or boogle(row + 1, col - 1, index + 1)
            or boogle(row - 1, col + 1, index + 1)
        )
        board[row][col] = temp
        return format

    for row in range(len(board)):
        for col in range(len(board[0])):
            if boogle(row, col, 0):
                return True

    return False
