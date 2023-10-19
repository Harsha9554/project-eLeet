import sys

from leets.stack.valid_parentheses_20 import valid_parentheses_20

sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(valid_parentheses_20(s))


main()
