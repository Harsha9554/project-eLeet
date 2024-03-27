import sys

from leets.binary_search.search_in_rotated_sorted_array_33 import (
    binary_search,
    search_in_rotated_sorted_array_33,
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
        k = int(input())
        print(search_in_rotated_sorted_array_33(nums, k))


main()
