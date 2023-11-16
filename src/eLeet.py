import sys

from leets.stack.generate_parentheses_22 import generate_parentheses_22


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(generate_parentheses_22(n))


main()
