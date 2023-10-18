import sys

from leets.two_pointers.three_sum_15 import three_sum_15


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
        print(three_sum_15(nums))


main()
