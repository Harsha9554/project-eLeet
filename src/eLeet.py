import sys

from leets.binary_search.find_minimum_in_rotated_sorted_array_153 import (
    find_minimum_in_rotated_sorted_array_153,
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
        nums = list(map(int, input().split()))
        print(find_minimum_in_rotated_sorted_array_153(nums))


main()
