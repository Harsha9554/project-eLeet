def is_valid_row(board):
    for i in range(9):
        num_set = set()
        for j in range(9):
            if board[i][j] == ".":
                continue
            elif board[i][j] not in num_set:
                num_set.add(board[i][j])
            else:
                return False
    return True


def is_valid_column(board):
    for j in range(9):
        num_set = set()
        for i in range(9):
            if board[i][j] == ".":
                continue
            elif board[i][j] not in num_set:
                num_set.add(board[i][j])
            else:
                return False
    return True


def get_key(i, j):
    x = i // 3
    y = j // 3
    return str(x) + str(y)


def is_valid_submatrix(board):
    # <-0-><-1--><-2-->
    # 5 3 . . 7 . . . .
    # 6 . . 1 9 5 . . .
    # . 9 8 . . . . 6 .
    # 8 . . . 6 . . . 3
    # 4 . . 8 . 3 . . 1
    # 7 . . . 2 . . . 6
    # . 6 . . . . 2 8 .
    # . . . 4 1 9 . . 5
    # . . . . 8 . . 7 9

    sub_matrix_dict = {}
    for i in range(3):
        for j in range(3):
            sub_matrix_dict[str(i) + str(j)] = set()

    for i in range(9):
        for j in range(9):
            key = get_key(i, j)
            num = board[i][j]
            if num == ".":
                continue
            elif num not in sub_matrix_dict[key]:
                sub_matrix_dict[key].add(num)
            else:
                return False
    return True


def valid_sudoku_36(board):
    # i'll try the brute force
    # check rows methods
    # check columns method
    # check sub matrices
    return is_valid_row(board) and is_valid_column(board) and is_valid_submatrix(board)


def valid_sudoku_36_ii(board):
    pass
