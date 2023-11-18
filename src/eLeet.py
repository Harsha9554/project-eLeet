import sys
from leets.stack.car_fleet_853 import car_fleet_853

from leets.stack.daily_temperatures_739 import daily_temperatures_739


sys.stdin = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/in.txt", "r"
)
sys.stdout = open(
    "/home/harsha9554/code/projects/active/project-eLeet/src/io/out.txt", "wt"
)


def main():
    t = int(input())
    for _ in range(t):
        target = int(input())
        position = list(map(int, input().split()))
        speed = list(map(int, input().split()))
        print(car_fleet_853(target, position, speed))


main()
