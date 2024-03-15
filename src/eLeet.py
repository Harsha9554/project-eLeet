import sys

from leets.sliding_window.minimum_window_substring_76 import minimum_window_substring_76


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        s, t = map(str, input().split())
        print(minimum_window_substring_76(s, t))


main()
