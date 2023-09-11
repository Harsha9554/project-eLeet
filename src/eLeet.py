import sys

from leets.arrays_and_hashing.valid_sudoku_36 import valid_sudoku_36


sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        board = []
        for _ in range(9):
            board.append(list(map(str, input().split())))
        print(valid_sudoku_36(board))


main()
