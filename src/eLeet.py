import sys

from leets.two_pointers.two_sum_ii_input_array_is_sorted_167 import (
    two_sum_ii_input_array_is_sorted_167,
)

sys.stdin = open("./io/in.txt", "r")
sys.stdout = open("./io/out.txt", "wt")


def main():
    t = int(input())
    for _ in range(t):
        nums = list(map(int, input().split()))
        target = int(input())
        print(two_sum_ii_input_array_is_sorted_167(nums, target))


main()
