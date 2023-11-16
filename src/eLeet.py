import sys

from leets.stack.evaluate_reverse_polish_notation_150 import (
    evaluate_reverse_polish_notation_150,
)


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        tokens = list(map(str, input().split()))
        print(evaluate_reverse_polish_notation_150(tokens))


main()
