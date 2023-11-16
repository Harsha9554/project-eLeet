import sys

from data_structures.stack import Stack


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    # t = int(input())
    # for _ in range(t):
    #     s = input()
    s = Stack()
    s.push("zeke")
    s.push("eren")
    s.push("reiner")
    s.pop()
    print(s.peek())
    print(s)


main()
