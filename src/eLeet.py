import sys

from leets.sliding_window.longest_repeating_character_replacement_424 import (
    longest_repeating_character_replacement_424,
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
        s = input()
        k = int(input())
        print(longest_repeating_character_replacement_424(s, k))


main()
