import sys

from leets.two_pointers.container_with_most_water_11 import container_with_most_water_11

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
        print(container_with_most_water_11(nums))


main()
