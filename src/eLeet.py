import sys

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
        temps = list(map(int, input().split()))
        print(daily_temperatures_739(temps))


main()
