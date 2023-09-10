import sys

from leets.arrays_and_hashing.two_sum_1 import two_sum_1


sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        target = int(input())
        print(two_sum_1(nums, target))


main()
