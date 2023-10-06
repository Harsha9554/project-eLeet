import sys

from leets.arrays_and_hashing.longest_consecutive_sequence_128 import (
    longest_consecutive_sequence_128,
)


sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        print(longest_consecutive_sequence_128(nums))


main()
