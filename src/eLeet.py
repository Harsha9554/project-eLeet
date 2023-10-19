import sys

from leets.two_pointers.trapping_rain_water_42 import trapping_rain_water_42

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
        print(trapping_rain_water_42(nums))


main()
